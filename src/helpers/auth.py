from datetime import datetime, timedelta
from os import getenv

from jose import jwt

JWT_SECRET = getenv("JWT_SECRET", "secret")
TIME_TO_TOKEN_EXPIRES_IN_MINUTES = int(getenv("TIME_TO_TOKEN_EXPIRES_IN_MINUTES", 30))


class Auth:
    @staticmethod
    def encode(token_dict: dict):
        to_encode = token_dict.copy()
        expire = datetime.utcnow() + timedelta(minutes=TIME_TO_TOKEN_EXPIRES_IN_MINUTES)
        to_encode.update({"exp": expire})
        return jwt.encode(token_dict, JWT_SECRET, algorithm="HS256")

    @staticmethod
    def decode(token: str):
        return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
