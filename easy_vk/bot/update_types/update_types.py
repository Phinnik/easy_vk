from pydantic import BaseModel, Field
from easy_vk.types.objects import MessagesMessage
from typing import Optional


class MessageNew(BaseModel):
    message: MessagesMessage = Field(...)
    client_info: dict = Field(...)


class MessageReply(MessagesMessage):
    ...


class MessageEdit(MessagesMessage):
    ...


class MessageAllow(BaseModel):
    user_id: int = Field(...)
    key: Optional[str] = Field(None)


class MessageDeny(BaseModel):
    user_id: int = Field(...)
