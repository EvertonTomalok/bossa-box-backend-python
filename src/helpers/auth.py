from datetime import datetime, timedelta
from functools import wraps
from os import getenv

from jose import ExpiredSignatureError, JWTError, jwt
from starlette.responses import Response

JWT_SECRET = getenv("JWT_SECRET", "secret")
TIME_TO_TOKEN_EXPIRES_IN_MINUTES = int(getenv("TIME_TO_TOKEN_EXPIRES_IN_MINUTES", 60))


def check_jwt(func):
    @wraps(func)
    async def decorated_view(*args, **kwargs):
        try:
            Auth.decode(kwargs.get("authorization"))
            return await func(*args, **kwargs)
        except ExpiredSignatureError:
            return Response(status_code=401, content="The token was expired.")
        except JWTError:
            return Response(status_code=403, content="Forbidden.")

    return decorated_view


class Auth:
    @staticmethod
    def encode(token_dict: dict):
        expire = datetime.utcnow() + timedelta(minutes=TIME_TO_TOKEN_EXPIRES_IN_MINUTES)
        token_dict.update({"exp": expire})
        return "Bearer " + jwt.encode(token_dict, JWT_SECRET, algorithm="HS256")

    @staticmethod
    def decode(token: str) -> dict:
        return jwt.decode(
            token.replace("Bearer ", ""), JWT_SECRET, algorithms=["HS256"]
        )
