from typing import List, Union


class Response:
    def __init__(self, data: Union[str, dict, List[dict]], code_status: int):
        self.data = data
        self.code_status = code_status

    def to_json(self):
        if 200 <= self.code_status < 400:
            return {
                "status": "ok",
                "data": self.data,
            }
        return {
            "status": "error",
            "error": self.data,
        }
