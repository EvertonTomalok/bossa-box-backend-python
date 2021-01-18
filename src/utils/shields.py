import logging
from functools import wraps

from starlette.responses import Response

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def shield_from_error(func, status_code_on_error=500):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            logger.critical(f"{func.__name__} -> {type(err)} - {err}")
            return Response(
                content="Something wrong went!", status_code=status_code_on_error
            )

    return decorated_view
