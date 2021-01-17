import logging

from src.repositories.tools import ToolsRepository
from src.utils.response import Response
from src.utils.shields import shield_from_error

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def _object_id_handler(o: dict):
    if "_id" in o:
        o["id"] = str(o["_id"])
        del o["_id"]
    return o


class ToolsController:
    @staticmethod
    @shield_from_error
    def add_tool(tool: dict) -> dict:
        data = ToolsRepository.insert_tool(tool)
        return Response(data=data, code_status=201).to_json()

    @staticmethod
    @shield_from_error
    def find_tools(tag: str = "", skip: int = 0, limit: int = 0):
        objects = ToolsRepository.find_tools(tag, skip, limit)
        data = [_object_id_handler(o) for o in objects]
        return Response(data=data, code_status=200).to_json()

    @staticmethod
    @shield_from_error
    def delete_tool(id: str) -> dict:
        ToolsRepository.delete_tool(id)
        return Response(data="", code_status=204).to_json()

    @staticmethod
    @shield_from_error
    def update_tool(id: str, tool) -> dict:
        if data := ToolsRepository.update_tool(id, tool):
            data = _object_id_handler(data)
            return Response(data=data, code_status=200).to_json()
        return {}
