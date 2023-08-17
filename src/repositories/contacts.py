from src.models.contacts import Contact
from src.utils.repository import SQLAlchemyRepository


class ContactsRepository(SQLAlchemyRepository):
    model = Contact
