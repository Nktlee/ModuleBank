from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from datetime import datetime

from src.database import Base

# print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))  # пример вывода: "2023-04-07 14:23:01"


class MessagesOrm(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    sender_name: Mapped[str] = mapped_column(String(100), nullable=False)
    text: Mapped[str] = mapped_column(String(500), nullable=False)
    user_message_count: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now().timestamp())
