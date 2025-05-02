from datetime import datetime

from fastapi import APIRouter

from src.schemas.messages import MessageRequestAdd, MessageAdd
from src.database import async_session_maker
from src.repositories.messages import MessagesRepository


router = APIRouter(prefix="/messages", tags=["Сообщения"])


@router.post("")
async def add_message(data: MessageRequestAdd):
    async with async_session_maker() as session:
        latest_message = await MessagesRepository(session).get_one_or_none(sender_name=data.sender_name)

        created_at = datetime.now()

        if latest_message:
            new_message_count = latest_message.user_message_count + 1
            _data = MessageAdd(**data.model_dump(), created_at=created_at, user_message_count=new_message_count)
        else:
            _data = MessageAdd(**data.model_dump(), created_at=created_at, user_message_count=1)

        await MessagesRepository(session).add(data=_data)
        await session.commit()

        return await MessagesRepository(session).get_ten()
