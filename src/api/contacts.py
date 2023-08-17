from fastapi import APIRouter
from fastapi_cache.decorator import cache

from src.api.dependencies import UOWDependency
from src.schemas.contacts import ContactCreate
from src.services.contacts import ContactsService

router = APIRouter(prefix="/contacts", tags=["Contacts"])


@router.post("")
async def add_contact(uow: UOWDependency, contact: ContactCreate):
    contact_id = await ContactsService().add_contact(uow=uow, contact=contact)
    return contact_id


@router.get("")
@cache(expire=60)
async def get_contacts(uow: UOWDependency, skip: int = 0, limit: int = 100):
    return await ContactsService().get_all_contacts(uow, skip=skip, limit=limit)


@router.get("/{contact_id}")
async def get_contact_by_id(uow: UOWDependency, contact_id: int):
    contact = await ContactsService().get_by_id(uow, contact_id)
    return contact


@router.patch("/{contact_id}")
async def edit_contact(contact_id: int, contact: ContactCreate, uow: UOWDependency):
    contact_id = await ContactsService().edit_contact(
        contact_id=contact_id, uow=uow, contact=contact
    )
    return contact_id


@router.delete("/{contact_id}")
async def delete_contact(uow: UOWDependency, contact_id: int):
    contact = await ContactsService().delete_contact(uow, contact_id)
    return contact
