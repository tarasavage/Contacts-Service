from typing import List, Dict, Optional

import httpx as httpx

from src.config.settings import settings


API_KEY = settings.API_KEY
URL = "https://api.nimble.com/api/v1/contacts"


async def scrape_resources(url: str) -> List[Dict]:
    headers = {"Authorization": f"Bearer {API_KEY}"}

    async with httpx.AsyncClient(headers=headers) as client:
        response = await client.get(url)
        return response.json().get("resources", [{}])


def filter_contacts(resources: List[Dict]) -> List[Dict]:
    return [resource for resource in resources if resource["record_type"] == "person"]


def extract_fullname_and_email(contact: Dict) -> Optional[Dict]:
    fields = contact.get("fields", {})

    if fields:
        first_name = fields.get("first name", [{}])[0].get("value", None)
        last_name = fields.get("last name", [{}])[0].get("value", None)
        email = fields.get("email", [{}])[0].get("value", None)

        return {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
        }


async def scrape_contacts() -> List[Dict]:
    resources = await scrape_resources(url=URL)
    contacts = filter_contacts(resources)
    return contacts
