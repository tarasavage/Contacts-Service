from src.schemas.schemas import ContactCreate
from src.utils.unit_of_work import IUnitOfWork


class ContactsService:
    @staticmethod
    async def add_contact(uow: IUnitOfWork, contact: ContactCreate):
        contact_dict = contact.model_dump()
        async with uow:
            contact_id = await uow.contacts.create(**contact_dict)
            await uow.commit()
            return contact_id

    @staticmethod
    async def edit_contact(
        uow: IUnitOfWork, contact_id: int, contact: ContactCreate
    ):
        contact_dict = contact.model_dump()
        async with uow:
            cur_id = await uow.contacts.update(instance_id=contact_id, **contact_dict)
            await uow.commit()
            return cur_id

    @staticmethod
    async def get_all_contacts(uow: IUnitOfWork, **kwargs):
        async with uow:
            contacts = await uow.contacts.get_all(**kwargs)
            return contacts

    @staticmethod
    async def get_by_id(uow: IUnitOfWork, contact_id: int):
        async with uow:
            contact = await uow.contacts.get_by_id(instance_id=contact_id)
            return contact

    @staticmethod
    async def delete_contact(uow: IUnitOfWork, contact_id: int):
        async with uow:
            contact = await uow.contacts.delete(instance_id=contact_id)
            await uow.commit()
            return contact
