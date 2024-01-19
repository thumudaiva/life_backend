from pydantic import BaseModel
from typing import Optional


class person(BaseModel):
    id:int
    first_name :str
    last_name :str
    email :str
    phone_number :str
    address :str
    country :str
    amount :float
    message :str

    class Config:
        from_attributes = True


class person_update(BaseModel):
    amount :float
    message :str

    class Config:
        from_attributes = True