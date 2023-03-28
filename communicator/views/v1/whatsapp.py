from communicator.views.serializer.whatsapp import WhatsApp
from fastapi import APIRouter


router = APIRouter(
    prefix="/whatsapp",
    tags=["whatsapp"])


@router.get("")
async def get():
    return {"Hello": "whatsapp"}


@router.post("/message/send", summary="Message Sender")
async def message_sender(item: WhatsApp):
    data = item.dict()
    return {"data": data}
