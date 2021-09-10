from logging import INFO, getLogger
from os import getenv
from typing import List

from pymongo import MongoClient, ReturnDocument

MONGODB_SETTINGS = {"url": getenv("MONGO_URL", "mongodb://mongo:mongo@localhost:27017")}

logger = getLogger()
logger.setLevel(INFO)


class MongoDBDatabase:
    __client = None
    __database = None
    __database_name = None

    def __init__(self, database_name, collection_name):
        self.collection_name = collection_name
        self.database_name = database_name
        self.__setup()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__teardown()

    def __del__(self):
        self.__teardown()

    def __setup(self):
        if not self.__client:
            self.__client = MongoClient(MONGODB_SETTINGS["url"])
        self.__database = self.__client[self.database_name]
        self.col = self.__database[self.collection_name]

    def __teardown(self):
        if self.__client:
            try:
                self.__client.close()
            except TypeError:
                pass

    def insert_update(self, data: dict, filter_to_update: dict):
        filter_to_update = filter_to_update

        self.col.update_one(
            filter_to_update,
            {"$set": data},
            upsert=True,
        )

    def find_one_and_update(self, filter: dict, update: dict):
        return self.col.find_one_and_update(
            filter, update, return_document=ReturnDocument.AFTER
        )

    def create_index(self, fields: List, index_name: str, expire_after_seconds=None):
        self.col.create_index(
            fields,
            name=index_name,
            background=True,
            expireAfterSeconds=expire_after_seconds,
        )
