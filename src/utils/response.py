from typing import List, Union


class Response:
    def __init__(self, data: Union[str, dict, List[dict]], code_status: int):
        self.data = data
        self.code_status = code_status

    def to_json(self):
        return {
            "status": "ok" if 200 <= self.code_status < 400 else "not ok",
            "data": self.data,
        }
