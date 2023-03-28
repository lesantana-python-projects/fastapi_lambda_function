from typing import Optional
from fastapi import Query
from pydantic import BaseModel
from pydantic.class_validators import validator
from communicator.configs import get_config

configs = get_config()


class WhatsApp(BaseModel):
    channel: Optional[str] = Query(...)
    messageType: Optional[str] = Query(...)
    from_: Optional[str] = Query(...)
    to: Optional[str] = Query(...)
    messageContent: Optional[str] = Query(...)

    class Config:
        fields = {
            'from_': 'from'
        }
        schema_extra = {
            "example": {
                "channel": "whatsapp",
                "messageType": "text",
                "from": "your_senderPhoneNumber",
                "to": "your_receiverPhoneNumber",
                "messageContent": "your_content"
            }
        }

    @validator("channel")
    def channel_type_validator(cls, value):
        if value not in configs.COMMUNICATOR_WHATSAPP_TYPES:
            raise ValueError('channel type is wrong.')
        return value
