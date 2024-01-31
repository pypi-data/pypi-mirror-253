from __future__ import annotations

class NotFoundError(Exception):
    pass

class UniqueError(Exception):
    pass

class HttpError(Exception):

    def __init__(self, msg: str, status_code: int, reason: str):
        self.status_code = status_code
        self.reason = reason
        super().__init__(msg)