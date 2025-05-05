from sqlalchemy import insert, select

from src.models.messages import MessagesOrm
from src.schemas.messages import Message, MessageAdd


class MessagesRepository:
    model = MessagesOrm
    schema = Message

    def __init__(self, session):
        self.session = session

    async def add(self, data: MessageAdd):
        add_data_stmt = (
            insert(self.model).values(**data.model_dump()).returning(self.model)
        )
        await self.session.execute(add_data_stmt)

    async def get_one_or_none(self, sender_name: str):
        query = (
            select(MessagesOrm)
            .filter(MessagesOrm.sender_name == sender_name)
            .order_by(MessagesOrm.created_at.desc())
            .limit(1)
        )
        result = await self.session.execute(query)
        model = result.scalars().one_or_none()
        if model is None:
            return None
        return self.schema.model_validate(model, from_attributes=True)

    async def get_ten(self) -> list[Message]:
        query = select(self.model).order_by(self.model.created_at.desc()).limit(10)
        result = await self.session.execute(query)
        models = [
            self.schema.model_validate(one, from_attributes=True)
            for one in result.scalars().all()
        ]

        return models
