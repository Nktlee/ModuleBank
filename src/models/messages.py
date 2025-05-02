from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from datetime import datetime

from src.database import Base


class MessagesOrm(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    sender_name: Mapped[str] = mapped_column(String(50), nullable=False)
    text: Mapped[str] = mapped_column(String(500), nullable=False)
    user_message_count: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[datetime]
