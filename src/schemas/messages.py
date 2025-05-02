from datetime import datetime

from pydantic import BaseModel


class MessageRequestAdd(BaseModel):
    sender_name: str
    text: str


class MessageAdd(BaseModel):
    sender_name: str
    text: str
    created_at: datetime
    user_message_count: int | None


class Message(MessageAdd):
    id: int
