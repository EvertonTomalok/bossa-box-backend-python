import logging
from functools import wraps

from src.utils.response import Response

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def shield_from_error(func, code_status_on_error=500):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            logger.critical(f"{func.__name__} -> {type(err)} - {err}")
            return Response(
                data={"msg": "Something went wrong!"}, code_status=code_status_on_error
            ).to_json()

    return decorated_view
