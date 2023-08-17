from sqlalchemy.orm import mapped_column, Mapped

from src.db.database import Base
from src.schemas.schemas import ContactRead


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(primary_key=True)

    first_name: Mapped[str]
    last_name: Mapped[str] = mapped_column(index=True, nullable=False)
    email: Mapped[str] = mapped_column(index=True, nullable=True, unique=True)

    def __str__(self) -> str:
        return f"Contact - First Name: {self.first_name}, Last Name: {self.last_name}, Email: {self.email}"

    def to_read_model(self) -> ContactRead:
        return ContactRead(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
        )
