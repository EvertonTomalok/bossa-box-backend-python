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
    404: {"model": Message, "description": "Something went wrong!"},
    201: {
        "description": "Item insert with success",
        "content": {
            "application/json": {"example": {"status": "ok", "data": data_example,}}
        },
    },
}

RESPONSE_RETURN_FIND_TOOL = {
    404: {"model": Message, "description": "Something went wrong!"},
    201: {
        "description": "Item insert with success",
        "content": {
            "application/json": {
                "example": {"status": "ok", "data": [data_example, data_example],}
            }
        },
    },
}
