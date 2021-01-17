from datetime import datetime, timedelta
from functools import wraps
from os import getenv

from jose import JWTError, jwt
from starlette.responses import Response

JWT_SECRET = getenv("JWT_SECRET", "secret")
TIME_TO_TOKEN_EXPIRES_IN_MINUTES = int(getenv("TIME_TO_TOKEN_EXPIRES_IN_MINUTES", 60))


class Auth:
    @staticmethod
    def encode(token_dict: dict):
        to_encode = token_dict.copy()
        expire = datetime.utcnow() + timedelta(minutes=TIME_TO_TOKEN_EXPIRES_IN_MINUTES)
        to_encode.update({"exp": expire})
        return jwt.encode(token_dict, JWT_SECRET, algorithm="HS256")

    @staticmethod
    def decode(token: str) -> dict:
        return jwt.decode(token, JWT_SECRET, algorithms=["HS256"],)


def check_jwt(func):
    @wraps(func)
    async def decorated_view(*args, **kwargs):
        try:
            Auth.decode(kwargs.get("token"))
            return await func(*args, **kwargs)
        except JWTError:
            return Response(status_code=401, content="Forbidden.")

    return decorated_view
