from bson import ObjectId

from src.adapters.mongodb.db import MongoDBDatabase


class ToolsRepository:
    @staticmethod
    def insert_tool(tool):
        with MongoDBDatabase("tools", "tools_collection") as db:
            operation_result = db.col.insert_one(tool)
            tool["id"] = str(operation_result.inserted_id)
            if "_id" in tool:
                del tool["_id"]
            return tool

    @staticmethod
    def find_tools(tag: str = "", skip: int = 0, limit: int = 0):
        with MongoDBDatabase("tools", "tools_collection") as db:
            _filter = {"tags": {"$in": [tag]}} if tag else {}
            return db.col.find(_filter, skip=skip, limit=limit)

    @staticmethod
    def delete_tool(id=str):
        with MongoDBDatabase("tools", "tools_collection") as db:
            return db.col.find_one_and_delete({"_id": ObjectId(id)})
