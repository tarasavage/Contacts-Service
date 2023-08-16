from typing import Optional

from pydantic import BaseModel, EmailStr, PositiveInt


class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: Optional[EmailStr]


class ContactCreate(ContactBase):
    pass


class ContactRead(ContactBase):
    id: PositiveInt

    class Config:
        from_attributes = True
