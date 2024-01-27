import asyncio
import importlib
import inspect
import os
import sys
import re

# import sys
import time
import traceback
import uuid
from typing import Optional, Set
from copy import deepcopy

from ..common.logger import logger
from ..common.queues import (
    GenericQueue,
    QueueMessage,
    QueueMessageType,
    QueueRole,
    QueueTopicMessage,
)
from ..common.stoppable import Stoppable
from ..common.storage import FileStorage
from ..common.types import (
    QUEUE_EVAL_TASKS,
    QUEUE_REPORTS,
    QUEUE_TOPICS,
    QUEUE_WORKER_TASKS,
    CrawlerBackTask,
    CrawlerContent,
    CrawlerHintURLStatus,
    CrawlerNop,
    DatapoolContentType,
    WorkerSettings,
    InvalidUsageException,
)


class CrawlerWorker(Stoppable):
    def __init__(self, cfg: Optional[WorkerSettings] = None):
        super().__init__()
        self.cfg = cfg if cfg is not None else WorkerSettings()
        self.id = uuid.uuid4().hex
        logger.info(f"worker id={self.id}")
        self.storage = FileStorage(self.cfg.STORAGE_PATH)
        self.todo_tasks: Set[asyncio.Task] = set()

        self.init_plugins()
        self.todo_queue = GenericQueue(
            role=QueueRole.Receiver,
            url=self.cfg.QUEUE_CONNECTION_URL,
            name=QUEUE_WORKER_TASKS,
            size=self.cfg.TODO_QUEUE_SIZE,
        )
        logger.info("created receiver worker_tasks")
        self.reports_queue = GenericQueue(
            role=QueueRole.Publisher,
            url=self.cfg.QUEUE_CONNECTION_URL,
            name=QUEUE_REPORTS,
        )
        logger.info("created publisher reports")
        self.producer_queue = GenericQueue(
            role=QueueRole.Publisher,
            url=self.cfg.QUEUE_CONNECTION_URL,
            name=QUEUE_EVAL_TASKS,
        )
        logger.info("created publisher eval_tasks")
        self.topics_queue = GenericQueue(
            role=QueueRole.Receiver,
            url=self.cfg.QUEUE_CONNECTION_URL,
            name=QUEUE_TOPICS,
            topic=CrawlerWorker.get_storage_invalidation_topic(self.id),
        )
        logger.info("created receiver topics")

        if self.cfg.CLI_MODE is True:
            self.stop_task_received = asyncio.Event()

    def run(self):
        # self.tasks.append( asyncio.create_task( self.tasks_fetcher_loop() ) )
        self.todo_queue.run()
        self.reports_queue.run()
        self.producer_queue.run()
        self.topics_queue.run()
        self.tasks.append(asyncio.create_task(self.worker_loop()))
        self.tasks.append(asyncio.create_task(self.topics_loop()))
        super().run()

    async def wait(self):
        """for CLI mode usage only"""
        if self.cfg.CLI_MODE is False:
            logger.error('worker invalid usage')
            raise InvalidUsageException("not a cli mode")
        await self.stop_task_received.wait()
        waiters = (
            self.todo_queue.until_empty(),
            self.reports_queue.until_empty(),
            self.producer_queue.until_empty(),
            self.topics_queue.until_empty(),
        )
        await asyncio.gather(*waiters)
        logger.info('worker wait done')

    async def stop(self):
        await super().stop()
        if len(self.todo_tasks) > 0:
            await asyncio.wait(
                self.todo_tasks, return_when=asyncio.ALL_COMPLETED
            )
        await self.todo_queue.stop()
        await self.reports_queue.stop()
        await self.producer_queue.stop()
        await self.topics_queue.stop()

        # for plugin_data in self.plugins:
        #     if plugin_data[0] is not None:
        #         logger.info( f'clearing plugin {plugin_data[1]}')
        #         plugin_data[0] = None
        #         plugin_data[1] = None

        logger.info("worker stopped")

    def init_plugins(self):
        self.plugins = []
        plugin_names = []

        plugins_dir = os.path.join(os.path.dirname(__file__), "plugins")
        logger.info(f"{plugins_dir=}")

        internal_plugins = []
        for dir in os.listdir(plugins_dir):
            if dir != "__pycache__" and os.path.isdir(
                os.path.join(plugins_dir, dir)
            ):
                internal_plugins.append(dir)
                if (
                    self.cfg.USE_ONLY_PLUGINS is None
                    or dir in self.cfg.USE_ONLY_PLUGINS
                ):
                    name = f"datapools.worker.plugins.{dir}"
                    plugin_names.append(name)

        if self.cfg.ADDITIONAL_PLUGINS is not None:
            for name in self.cfg.ADDITIONAL_PLUGINS:
                if importlib.util.find_spec(name):
                    plugin_names.append(name)

#        logger.info( f'BEFORE:{sys.modules=}')
        for name in plugin_names:
            if name not in sys.modules:
                logger.info(f"loading module {name}")
                module = importlib.import_module(name)
            else:
                logger.info(f"RE-loading module {name}")
                module = importlib.reload(sys.modules[name])

            clsmembers = inspect.getmembers(module, inspect.isclass)
            # logger.info( f'{clsmembers=}')

            for cls in clsmembers:
                for base in cls[1].__bases__:
                    # logger.info( f'{base=}')
                    if base.__name__ == "BasePlugin":
                        # logger.info( f'valid plugin class {cls[1]}')
                        self.plugins.append([None, cls])  # obj, class
                        break
        # logger.info( f'AFTER:{sys.modules=}')

    async def topics_loop(self):
        # from Producer.Evaluator - receives storage_id which content can be removed
        try:
            while not await self.is_stopped():
                message = await self.topics_queue.pop(timeout=1)
                if message:
                    qm = QueueTopicMessage.decode(
                        message.routing_key, message.body
                    )
                    if (
                        message.routing_key
                        == CrawlerWorker.get_storage_invalidation_topic(
                            self.id
                        )
                    ):
                        logger.info(
                            f"invalidating storage {qm.data[ 'storage_id' ]}"
                        )
                        await self.storage.remove(qm.data["storage_id"])

                        await self.topics_queue.mark_done(message)
                    else:
                        logger.error(
                            f"!!!!!!!!!!!!!!! BUG: unexpected topic {message=} {qm=}"
                        )
                        await self.topics_queue.reject(message, requeue=False)
        except Exception as e:
            logger.error(f"!!!!!!!!Exception in topics_loop() {e}")
            logger.error(traceback.format_exc())

    async def worker_loop(self):
        # fetches urls one by one from the queue and scans them using available plugins
        try:
            while not await self.is_stopped():
                message = await self.todo_queue.pop(timeout=1)
                if message:
                    task = asyncio.create_task(
                        self._process_todo_message(message)
                    )
                    self.todo_tasks.add(task)
                    task.add_done_callback(self.todo_tasks.discard)

        except Exception as e:
            logger.error(f"!!!!!!!!Exception in worker_loop() {e}")
            logger.error(traceback.format_exc())

    async def _process_todo_message(self, message):
        qm = QueueMessage.decode(message.body)

        if qm.type == QueueMessageType.Task:
            done = False

            task = qm.data
            logger.info(f"got {task=}")
            if type(task) is dict and "url" in task:
                url = task["url"]
                logger.info(f"processing {url=}")

                plugin = self._get_url_plugin(url)
                logger.info(f"suitable {plugin=}")

                if plugin is None:
                    await self.todo_queue.reject(message, requeue=False)
                    return

                last_processing_notification = 0
                for attempt in range(0, self.cfg.ATTEMPTS_PER_URL):

                    if await self.is_stopped():
                        break
                    if attempt > 0:
                        logger.info(f"{attempt=}")

                    try:
                        async for content_or_task in plugin.process(url):
                            # logger.info( f'{type( content_or_task )=}')
                            t = type(content_or_task)
                            # logger.info( f'{(t is CrawlerNop)=}')
                            if t is CrawlerContent:
                                # notifying datapool pipeline about new crawled data
                                await self.producer_queue.push(
                                    QueueMessage(
                                        QueueMessageType.Task,
                                        {
                                            "parent_url": url,
                                            "url": content_or_task.url,
                                            "storage_id": content_or_task.storage_id,
                                            "tag_id": content_or_task.tag_id,
                                            "copyright_tag_id": content_or_task.copyright_tag_id,
                                            "platform_tag_id": content_or_task.platform_tag_id,
                                            "type": DatapoolContentType(
                                                content_or_task.type
                                            ).value,
                                            "worker_id": self.id,
                                        },
                                    )
                                )

                            elif t is CrawlerBackTask:
                                await self._add_back_task(content_or_task)
                            elif t is CrawlerNop:
                                pass
                            else:
                                raise Exception(f"unknown {content_or_task=}")

                            # notifying backend that we are alive from time to time
                            now = time.time()
                            if now - last_processing_notification > 5:
                                await self._set_task_status(
                                    task,
                                    CrawlerHintURLStatus.Processing,
                                )
                                last_processing_notification = now

                            # logger.info( '=================================== process iteration done')

                        logger.info("plugin.process done")
                        await self._set_task_status(
                            task, CrawlerHintURLStatus.Success
                        )

                        done = True
                        break
                    except Exception as e:
                        logger.error(f"failed get url: {e}")
                        logger.error(traceback.format_exc())
                        await asyncio.sleep(self.cfg.ATTEMPTS_DELAY)
                    if done:
                        break

                plugin.is_busy = False

            if done:
                logger.info(f"sending ack for {message.message_id=}")
                await self.todo_queue.mark_done(message)
            else:
                logger.info(f"sending reject for {message.message_id=}")
                await self.todo_queue.reject(message, requeue=False)
                await self._set_task_status(task, CrawlerHintURLStatus.Failure)

        elif qm.type == QueueMessageType.Stop:
            await self.todo_queue.mark_done(message)
            logger.info('worker: got stop task')

            await self.producer_queue.push(
                QueueMessage(
                    QueueMessageType.Stop
                )
            )
            # notifying scheduler that we are done
            await self.reports_queue.push(
                QueueMessage(
                    QueueMessageType.Stop
                )
            )
            self.stop_task_received.set()

        else:
            logger.error(f"!!!!!!!!!!!!!!! BUG: unexpected {message=} {qm=}")
            await self.todo_queue.reject(message)

    # async def _set_task_status( self, task, status: CrawlerHintURLStatus, contents = None ):
    #     await self.reports_queue.push( QueueMessage( QueueMessageType.Report, { 'task': task, 'status': status.value, 'contents': contents } ) )

    async def _set_task_status(self, task, status: CrawlerHintURLStatus):
        await self.reports_queue.push(
            QueueMessage(
                QueueMessageType.Report, {"task": deepcopy(task), "status": status.value}
            )
        )

    async def _add_back_task(self, task: CrawlerBackTask):
        await self.reports_queue.push(
            QueueMessage(QueueMessageType.Task, task.to_dict())
        )

    def _get_plugin_object(self, cls):
        args = [self.storage]
        kwargs = {}
        logger.info(f"_get_plugin_object {cls=}")

        # convert class name into config plugins key
        # example: GoogleDrivePlugin => google_drive
        # example: S3Plugin => s3
        cap_words = re.sub(r'([A-Z])', r' \1', cls[0]).split()
        logger.info(f'{cap_words=}')
        config_key = '_'.join(list(map(lambda x: x.lower(), cap_words[:-1])))
        logger.info(f'{config_key=}')
        plugin_config = self.cfg.plugins_config.get(config_key)
        logger.info(f'{plugin_config=}')
        if plugin_config is not None:
            # plugin config dict keys must match plugin's class __init__ arguments
            kwargs = plugin_config

        return cls[1](*args, **kwargs)

    def _get_url_plugin(self, url):
        for plugin_data in self.plugins:
            cls = plugin_data[1]
            if cls[0] != "DefaultPlugin":
                if cls[1].is_supported(url):
                    if plugin_data[0] is None:
                        plugin_data[0] = self._get_plugin_object(cls)
                    if not plugin_data[0].is_busy:
                        plugin_data[0].is_busy = True
                        return plugin_data[0]
                    else:
                        new_obj = self._get_plugin_object(cls)
                        new_obj.is_busy = True
                        return new_obj

        # creating/usingexisting default plugin
        for plugin_data in self.plugins:
            cls = plugin_data[1]
            if cls[0] == "DefaultPlugin":
                if cls[1].is_supported(url):
                    if plugin_data[0] is None:
                        plugin_data[0] = self._get_plugin_object(cls)
                    if not plugin_data[0].is_busy:
                        plugin_data[0].is_busy = True
                        return plugin_data[0]
                    else:
                        new_obj = self._get_plugin_object(cls)
                        new_obj.is_busy = True
                        return new_obj
                else:
                    raise Exception(f"default plugin does not support {url=}")

    @staticmethod
    def get_storage_invalidation_topic(id):
        return (
            f"worker.id_{id}.type_{QueueMessageType.StorageInvalidation.value}"
        )
