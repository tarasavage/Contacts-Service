from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.db.database import Base
from src.schemas.users import UserRead


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(80), index=True, nullable=False)
    last_name = Column(String(80), index=True, nullable=False)
    email = Column(String(80), index=True, nullable=True, unique=True)

    def __str__(self) -> str:
        return f"Contact - First Name: {self.first_name}, Last Name: {self.last_name}, Email: {self.email}"

    def to_read_model(self) -> UserRead:
        return UserRead(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
        )
