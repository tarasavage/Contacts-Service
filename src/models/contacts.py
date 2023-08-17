from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import mapped_column, Mapped

from src.db.database import Base
from src.models.users import User
from src.schemas.contacts import ContactRead


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str] = mapped_column(
        String(length=255), index=True, nullable=False
    )
    address: Mapped[str] = mapped_column(String(length=255), nullable=False)
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(User.id), index=True, nullable=False
    )

    def __str__(self) -> str:
        return f"Contact - First Name: {self.first_name}, Last Name: {self.last_name}"

    def to_read_model(self) -> ContactRead:
        return ContactRead(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            address=self.address,
        )
