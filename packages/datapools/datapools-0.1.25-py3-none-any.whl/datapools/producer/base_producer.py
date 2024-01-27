import asyncio

# import importlib
# import inspect
import os

# import sys
import traceback

# from enum import Enum
from typing import List, Optional

from ..common.backend_api import BackendAPI#, TagDatapool
from ..common.logger import logger
from ..common.queues import (
    GenericQueue,
    QueueMessage,
    QueueMessageType,
    QueueRole,
    QueueTopicMessage,
)
from ..common.stoppable import Stoppable
from ..common.storage.file_storage import FileStorage
from ..common.types import QUEUE_EVAL_TASKS  # QUEUE_WORKER_TASKS,
from ..common.types import (
    QUEUE_TOPICS,
    BaseProducerSettings,
    DatapoolContentType,
    #DatapoolRuleMatch,
    #DatapoolRules,
    InvalidUsageException,
)
from ..worker import CrawlerWorker
#from .rules import DatapoolRulesChecker

class BaseProducer(Stoppable):
    def __init__(self, cfg: Optional[BaseProducerSettings] = None):
        super().__init__()
        self.cfg = cfg if cfg is not None else BaseProducerSettings()

        if not self.cfg.CLI_MODE:
            self.api = BackendAPI(url=self.cfg.BACKEND_API_URL)

        # receives tasks from workers
        self.eval_queue = GenericQueue(
            role=QueueRole.Receiver,
            url=self.cfg.QUEUE_CONNECTION_URL,
            name=QUEUE_EVAL_TASKS,
        )
        logger.error("created receiver eval_tasks")

        # will invalidate worker cache entries
        self.topics_queue = GenericQueue(
            role=QueueRole.Publisher,
            url=self.cfg.QUEUE_CONNECTION_URL,
            name=QUEUE_TOPICS,
            topic=True,  # for Rabbitmq publisher
        )
        logger.info("created publisher worker_tasks")
        if self.cfg.CLI_MODE is True:
            self.stop_task_received = asyncio.Event()

        #self.datapool_rules_checker = DatapoolRulesChecker()

    def run(self):
        self.tasks.append(asyncio.create_task(self.router_loop()))
        self.eval_queue.run()
        self.topics_queue.run()
        super().run()

    async def wait(self):
        if self.cfg.CLI_MODE is False:
            logger.error( 'baseproducer invalid usage')
            raise InvalidUsageException("not a cli mode")
        
        await self.stop_task_received.wait()
        waiters = (
            self.eval_queue.until_empty(),
            self.topics_queue.until_empty(),
        )
        await asyncio.gather(*waiters)
        logger.info( 'BaseProducer wait done')

    async def stop(self):
        await self.eval_queue.stop()
        await self.topics_queue.stop()
        await super().stop()
        logger.info("base producer stopped")

    async def router_loop(self):
        try:
            while not await self.is_stopped():
                message = await self.eval_queue.pop(timeout=1)
                if message:
                    qm = QueueMessage.decode(message.body)
                    try:
                        if qm.type == QueueMessageType.Task:
                            task = qm.data
                            logger.info(f"Producer got: {task}")

                            # TODO: this storage must be associated with the worker!
                            #   For example, storage path or url can be formatted accordingly to worker id
                            worker_storage = FileStorage(
                                self.cfg.WORKER_STORAGE_PATH
                            )
                            raw_data = await worker_storage.get(task["storage_id"])
                            await self.process_content(raw_data, task)

                            # datapools = await self._get_tag_datapools(
                            #     task["tag_id"]
                            # )
                            # logger.info(f"tag_id {task['tag_id']} in {datapools=}")
                            # for datapool_data in datapools:
                            #     logger.info(
                            #         f"matching content for {datapool_data.id=}"
                            #     )
                            #     against = DatapoolRuleMatch(
                            #         content_type=task[
                            #             "type"
                            #         ],  # DatapoolContentType
                            #         url=task[
                            #             "parent_url"
                            #         ],  # for image it should be site image, not image src itself
                            #     )
                            #     if self.datapool_rules_checker.match(
                            #         datapool_data.rules, against
                            #     ):
                            #         logger.info("matched")
                            #         await self.process_content(
                            #             datapool_data.id, raw_data, task
                            #         )
                            #     else:
                            #         logger.info("not matched")

                            # tell worker that his storage item can be removed
                            await self.topics_queue.push(
                                QueueTopicMessage(
                                    CrawlerWorker.get_storage_invalidation_topic(
                                        task["worker_id"]
                                    ),
                                    {"storage_id": task["storage_id"]},
                                )
                            )
                        elif qm.type == QueueMessageType.Stop:
                            logger.info( 'base_producer: stop task received')
                            self.stop_task_received.set()
                        else:
                            raise Exception(f"!!!!!!!!!!!!!!! BUG: unexpected {message=} {qm=}")

                        await self.eval_queue.mark_done(message)
                    except Exception as e:
                        logger.error(f"Catched: {traceback.format_exc()}")
                        logger.error(f"failed evaluate {e}")
                        await self.eval_queue.reject(message)

        except Exception as e:
            logger.error(f"Catched: {traceback.format_exc()}")
            logger.error(f"!!!!!!! Exception in Datapools::router_loop() {e}")

    # async def _get_tag_datapools(self, tag_id) -> List[TagDatapool]:
    #     if not self.cfg.CLI_MODE:
    #         # TODO: tag_id: datapool_ids pairs should be cached with cache TTL:
    #         #   CACHE CONSIDERATION: user may leave datapool while datapool_id may still be associated with tag_id in cache
    #         return await self.api.get_tag_datapools(tag_id)
    #     return [
    #         TagDatapool(
    #             id=1,
    #             rules=DatapoolRules(
    #                 content_type=[
    #                     DatapoolContentType.Text,
    #                     DatapoolContentType.Image,
    #                     DatapoolContentType.Video,
    #                     DatapoolContentType.Audio,
    #                 ],
    #             ),
    #         )
    #     ]

    async def process_content(self, 
                              #datapool_id,
                              raw_data, task):
        #path = os.path.join(self.cfg.STORAGE_PATH, str(datapool_id))
        path = self.cfg.STORAGE_PATH
        if not os.path.exists(path):
            os.mkdir(path)
        storage = FileStorage(path)
        # put data into persistent storage
        await storage.put(
            task["storage_id"], raw_data
        )  # TODO: consider using datapool_id
