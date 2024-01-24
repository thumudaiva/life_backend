from pydantic import BaseModel
from typing import Optional


class contactquery(BaseModel):
    id:int
    first_name :str
    email :str
    phone_number :str
    subject :str
    message :str

    class Config:
        from_attributes = True


class donation(BaseModel):
    id:int
    first_name :str
    last_name :str
    email :str
    phone_number :str
    address :str
    country :str
    amount :float
    reference :str
    message :str

    class Config:
        from_attributes = True


class prayerrequest(BaseModel):
    id:int
    first_name :str
    last_name :str
    email :str
    phone_number :str
    address :str
    country :str
    message :str

    class Config:
        from_attributes = True

