from src.models.routes import Message

data_example = {
    "title": "hotel",
    "link": "https://github.com/typicode/hotel",
    "description": (
        "Local app manager. Start apps within your browser, developer tool with local"
        " .localhost domain and https out of the box."
    ),
    "tags": ["Java", "gcloud", "webapps"],
    "id": "600258be6976172455f7ca1a",
}

RESPONSE_RETURN_POST_TOOL = {
    "404": {"model": Message, "description": "Something went wrong!"},
    "201": {
        "description": "Item insert with success",
        "content": {
            "application/json": {"example": {"status": "ok", "data": data_example,}}
        },
    },
}

RESPONSE_RETURN_PUT_TOOL = {
    "404": {"model": Message, "description": "Something went wrong!"},
    "200": {
        "description": "Item updated with success",
        "content": {
            "application/json": {"example": {"status": "ok", "data": data_example}}
        },
    },
    "204": {"description": "No item Found"},
}


RESPONSE_RETURN_FIND_TOOL = {
    "404": {"model": Message, "description": "Something went wrong!"},
    "201": {
        "description": "Item insert with success",
        "content": {
            "application/json": {
                "example": {"status": "ok", "data": [data_example, data_example]}
            }
        },
    },
}

RESPONSE_RETURN_TOKEN = {
    "404": {"model": Message, "description": "Something went wrong!"},
    "201": {
        "description": "Token created with success",
        "content": {
            "application/json": {
                "example": {
                    "status": "ok",
                    "data": {
                        "token": (
                            "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiRXZlcnRvbiBUb21hbG9rIn0."
                            "OroiSjd5H1R3e1AexgP8US6UxHopAZDOHZ6jE09CyMQ"
                        )
                    },
                }
            }
        },
    },
}
