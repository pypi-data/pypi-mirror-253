from ....common.logger import logger
from ....common.types import CrawlerNop
from ..base_plugin import BasePlugin


class DefaultPlugin(BasePlugin):
    def __init__(self, storage):
        super().__init__(storage)

    @staticmethod
    def is_supported(url):
        return True

    async def process(self, url):
        yield CrawlerNop
        # raise Exception("DefaultPlugin::process() is not implemented")
