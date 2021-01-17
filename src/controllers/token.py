from src.helpers.auth import Auth


class TokenController:
    @staticmethod
    def create_token(token_dict: dict):
        return {"status": "ok", "data": {"token": Auth.encode(token_dict)}}
