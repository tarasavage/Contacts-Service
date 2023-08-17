from celery import Celery
from celery.schedules import crontab

from src.config.settings import settings
from src.schemas.contacts import ContactCreate
from src.services.contacts import ContactsService
from src.utils.async_to_sync import async_to_sync
from src.utils.scraper import extract_fullname_and_email, scrape_contacts
from src.utils.unit_of_work import UnitOfWork

celery = Celery("tasks", broker=settings.CELERY_BROKER_URL)


celery.conf.beat_schedule = {
    "scrape_contacts_and_insert_at_8_00": {
        "task": "tasks.scrape_contacts_and_insert",
        "schedule": crontab(hour=8, minute=0),
    },
}

celery.conf.timezone = "UTC"


@celery.task
@async_to_sync
async def scrape_contacts_and_insert():
    contacts = await scrape_contacts()
    await insert_contacts_into_db(contacts)


async def insert_contacts_into_db(contacts: list) -> None:
    for contact in contacts:
        contact_db = ContactCreate(**extract_fullname_and_email(contact))
        await ContactsService().add_contact(UnitOfWork(), contact_db)
