from pydantic import BaseModel, PositiveInt


class ContactBase(BaseModel):
    first_name: str
    last_name: str
    address: str
    user_id: int


class ContactCreate(ContactBase):
    pass


class ContactRead(ContactBase):
    id: PositiveInt

    class Config:
        from_attributes = True
