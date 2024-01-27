import asyncio
import copy

# import json
# import time
import traceback
from typing import Optional

from .common.backend_api import BackendAPI
from .common.logger import logger
from .common.queues import (
    GenericQueue,
    QueueMessage,
    QueueMessageType,
    QueueRole,
)
from .common.stoppable import Stoppable

# from .common.tasks_db import Hash
# from .common.tasks_db.redis import RedisTasksDB
from .common.types import (
    QUEUE_REPORTS,
    QUEUE_WORKER_TASKS,
    CrawlerHintURLStatus,
    SchedulerSettings,
    InvalidUsageException,
)

# import httpx

class CrawlerScheduler(Stoppable):
    # 1. task:
    #   - get hint urls from the backend, put into tasks_db, status is changed at the backend at once
    #   - check "processing" tasks: ping worker. If it's dead then task is moved back to the queue
    # 2. api: get urls from workers, put into tasks_db
    #   tips:
    #   - reject existing urls: request redis by url hash
    # 3. api: worker gets a new task(s?) from queue:
    #   tips:
    #   - tasks_db: (redis) task should be moved into a separate key as "in progress", worker ID/IP/etc should be remembered to be able to ping
    # 4. api: worker notifies about finished task
    #    - remove task from "processing"
    #    - if it's a backend hint url, then update its status by calling backend api

    hints: Optional[asyncio.Queue] = None
    def __init__(self, cfg: Optional[SchedulerSettings] = None):
        super().__init__()
        self.cfg = cfg if cfg is not None else SchedulerSettings()

        if self.cfg.CLI_HINT_URLS is not None:
            #self.hints_done = asyncio.Event()
            self.hints = asyncio.Queue()
            for url in self.cfg.CLI_HINT_URLS:
                self.hints.put_nowait( url )
            self.hints.put_nowait('')  #empty string as a marker of the list end
        elif self.cfg.CLI_MODE is True:
            #self.hints_done = asyncio.Event()
            self.hints = asyncio.Queue()
        else:
            self.api = BackendAPI(url=self.cfg.BACKEND_API_URL)
            

        # self.tasks_db = RedisTasksDB(
        #     host=self.cfg.REDIS_HOST, port=self.cfg.REDIS_PORT
        # )
        self.todo_queue = GenericQueue(
            role=QueueRole.Publisher,
            url=self.cfg.QUEUE_CONNECTION_URL,
            name=QUEUE_WORKER_TASKS,
        )
        logger.info("created publisher worker_tasks")
        self.reports_queue = GenericQueue(
            role=QueueRole.Receiver,
            url=self.cfg.QUEUE_CONNECTION_URL,
            name=QUEUE_REPORTS,
        )
        logger.info("created receiver reports")
        
        if self.cfg.CLI_MODE:
            # TODO: this mechanism will not work for multiple workers/producers
            self.stop_task_processed = asyncio.Event()

    async def wait(self):
        """for CLI mode usage only"""
        if self.cfg.CLI_HINT_URLS is None and self.cfg.CLI_MODE is False:
            logger.error( 'scheduler invalid usage')
            raise InvalidUsageException("not a cli mode")
        
        await self.stop_task_processed.wait()
        
        waiters = ( #self.hints_done.wait(),
                   self.todo_queue.until_empty(),
                   self.reports_queue.until_empty(),
                )
        await asyncio.gather(*waiters)
        logger.info( 'scheduler wait done')

    def run(self):
        self.tasks.append(asyncio.create_task(self.hints_loop()))
        self.tasks.append(asyncio.create_task(self.reports_loop()))
        self.todo_queue.run()
        self.reports_queue.run()
        super().run()

    async def stop(self):
        logger.info("scheduler stopping")
        await self.todo_queue.stop()
        logger.info("todo_queue stopped")
        await self.reports_queue.stop()
        logger.info("reports_queue stopped")
        await super().stop()
        logger.info("super stopped")

    async def _set_task_status(self, data):
        # hash, status: CrawlerHintURLStatus, contents
        logger.info(f"set_task_status: {data=}")
        task = data["task"]
        status = CrawlerHintURLStatus(data["status"])
        # contents = data[ 'contents' ]

        # if status == CrawlerHintURLStatus.Success:
        #     logger.info("------------------ task done --------------------")
        #     self.tasks_db.set_done(task["_hash"])

        if "id" in task:
            logger.info(f"--------------- set hint url status {status}")
            # this is hint url from server => have to update status on the backend
            if self.cfg.CLI_HINT_URLS is None:
                await self.api.set_hint_url_status(task["id"], status)

        # if contents:
        #     logger.info( f'----------------- pushing contents {contents=}' )
        #     await self.api.add_crawler_contents( contents )

    async def _add_task(self, task: dict, ignore_existing=False, ignore_done=False):
        # puts task to the todo_queue if it does not exist in new/done list
        # hash = self.tasks_db.add(
        #     task, ignore_existing=ignore_existing, ignore_done=ignore_done
        # )
        # if hash:
        # task["_hash"] = hash
        #logger.info( 'pushing to worker_tasks')
        if 'stop_running' not in task:
            await self.todo_queue.push(
                    QueueMessage(QueueMessageType.Task, data=task)
            )
        else:
            await self.todo_queue.push(
                    QueueMessage(QueueMessageType.Stop)
            )
            
        #logger.info( 'pushed')
        return True
        # return hash

    # return False
    
    async def add_hint(self, url):
        """for cli mode: pushing url to the queue. Scheduler will run until empty string is added"""
        await self.hints.put(url)

    async def _get_hint_urls(self):
        hints = None
        if self.cfg.CLI_HINT_URLS is None and self.cfg.CLI_MODE is False:
            # deployment mode
            try:
                hints = await self.api.get_hint_urls(limit=10)
            except Exception as e:
                logger.error(f"Failed get hints: {e}")
        else:
            # cli mode
            try:
                url = await asyncio.wait_for( self.hints.get(), timeout=1 )
                if len(url) > 0:
                    hints = [{"url": url}]
                else:
                    hints = [{'stop_running':True}]
                #    self.stop_task_received.set()
                #     logger.info( 'hints_done' )
                #     self.hints_done.set()
            except asyncio.TimeoutError:
                pass
        return hints

    async def hints_loop(self):
        # infinitely fetching URL hints by calling backend api
        try:
            while not await self.is_stopped():
                if True:  # self.tasks_db.is_ready():
                    hints = await self._get_hint_urls()
                    if hints is not None:
                        for hint in hints:
                            logger.info(f"got hint: {hint}")

                            ignore_existing = True  # TODO: for tests only!
                            if not await self._add_task(
                                hint,
                                ignore_existing=ignore_existing,
                                ignore_done=True,
                            ):
                                logger.error( 'failed add task, REJECTING')
                                if "id" in hint:
                                    await self.api.set_hint_url_status(
                                        hint["id"],
                                        CrawlerHintURLStatus.Rejected,
                                    )
                if self.cfg.CLI_HINT_URLS is None and self.cfg.CLI_MODE is False:
                    await asyncio.sleep(self.cfg.BACKEND_HINTS_PERIOD)
        except Exception as e:
            logger.error(
                f"!!!!!!! Exception in CrawlerScheduler::hints_loop() {e}"
            )
            logger.error(traceback.format_exc())

    async def reports_loop(self):
        # receive reports from workers
        try:
            while not await self.is_stopped():
                message = await self.reports_queue.pop(timeout=1)
                if message:
                    try:
                        qm = QueueMessage.decode(message.body)
                        if qm.type == QueueMessageType.Task:
                            logger.info("new task from worker")
                            # logger.info(f"{qm=}")
                            await self._add_task(qm.data, ignore_done=True)
                        elif qm.type == QueueMessageType.Report:
                            await self._set_task_status(qm.data)
                        elif qm.type == QueueMessageType.Stop:
                            logger.info( 'scheduler: got stop from worker')
                            self.stop_task_processed.set()
                        else:
                            logger.error(f"Unsupported QueueMessage {qm=}")

                    except Exception as e:
                        logger.error(f"Failed decode process report")
                        logger.error(traceback.format_exc())

                    await self.reports_queue.mark_done(message)

        except Exception as e:
            logger.error(
                f"!!!!!!! Exception in CrawlerScheduler::reports_loop() {e}"
            )
            logger.error(traceback.format_exc())
