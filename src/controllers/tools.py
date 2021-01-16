import logging
from functools import wraps

from src.repositories.tools import ToolsRepository
from src.utils.response import Response

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def shield_from_error(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            logger.critical(f"{func.__name__} -> {type(err)} - {err}")
            return Response(
                data={"msg": "Something went wrong!"}, code_status=500
            ).to_json()

    return decorated_view


@shield_from_error
def add_tool(tool: dict) -> dict:
    data = ToolsRepository.insert_tool(tool)
    return Response(data=data, code_status=201).to_json()


@shield_from_error
def find_tools(tag: str = "", skip: int = 0, limit: int = 0):
    def _object_handler(o: dict):
        o["id"] = str(o["_id"])
        del o["_id"]

        return o

    objects = ToolsRepository.find_tools(tag, skip, limit)
    data = [_object_handler(o) for o in objects]
    return Response(data=data, code_status=200).to_json()
