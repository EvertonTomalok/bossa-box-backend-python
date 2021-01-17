from src.controllers.token import TokenController


def test_token():
    token = TokenController.create_token({"user": "any_user"})
    assert token.get("status") == "ok"
