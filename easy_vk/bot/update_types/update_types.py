from pydantic import BaseModel, Field
from easy_vk.types.objects import MessagesMessage


class MessageNew(BaseModel):
    message: MessagesMessage = Field(...)
    client_info: dict = Field(...)

