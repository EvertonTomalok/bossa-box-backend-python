from typing import List

from pydantic import BaseModel


class Message(BaseModel):
    status: str = "error"
    data: dict = {"msg": "Something went wrong!"}


class Tool(BaseModel):
    title: str
    link: str
    description: str
    tags: List[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "Notion",
                "link": "https://notion.so",
                "description": (
                    "All in one tool to organize teams and ideas. Write, plan, collaborate, and get organized. "
                ),
                "tags": [
                    "organization",
                    "planning",
                    "collaboration",
                    "writing",
                    "calendar",
                ],
            }
        }
