from typing import TypedDict


class SMSEventDict(TypedDict):
    to: str
    message: str
