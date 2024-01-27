from hashlib import md5


class BaseStorage:
    async def put(self, storage_id, content):
        raise Exception("implement put()")

    async def get(self, storage_id):
        raise Exception("implement get()")

    async def remove(self, storage_id):
        raise Exception("implement remove()")

    @staticmethod
    def gen_id(data):
        return md5(data.encode()).hexdigest()
