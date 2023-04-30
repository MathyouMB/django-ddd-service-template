from enum import Enum


class ErrorType(Enum):
    RECORD_NOT_FOUND = 1
    VALIDATION = 2
    FAILED_TO_CREATE = 3


class Error:
    def __init__(self, message: str, type: ErrorType):
        self.message = message
        self.type = type
