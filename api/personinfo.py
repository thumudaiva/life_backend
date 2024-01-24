from fastapi import APIRouter, Depends
from typing import List
from schemas.schemas import  contactquery, donation, prayerrequest
from models.model import ContactQuery, Donation, PrayerRequest
from sqlalchemy.orm import Session
from init_db import get_db

router = APIRouter()

#@router.get("/personifo", response_model=List[person])
#async def get_all_persons(db: Session = Depends(get_db)):
#    person = db.query(Personinfo).all()
#    return person

#@router.get("/country", response_model=List[person])
#async def get_all_countries(db: Session = Depends(get_db)):
#    person = db.query(country).all()
##    return person


@router.post("/contactquery", response_model=contactquery)
def create_contact_query(p: contactquery, db: Session = Depends(get_db)):
    import uuid
    contactquery = ContactQuery(
    id = p.id,
    first_name = p.first_name,
    email=p.email,
    phone_number =p.phone_number,
    subject=p.subject,
    message = p.message )

    db.add(contactquery)
    db.commit()
    db.refresh(contactquery)
    return contactquery

@router.post("/donation", response_model=donation)
def create_donation(p: donation, db: Session = Depends(get_db)):
    import uuid
    donation = Donation(
    id = p.id,
    first_name = p.first_name,
    last_name = p.last_name,
    email=p.email,
    phone_number =p.phone_number,
    address = p.address,
    country =p.country,
    amount = p.amount,
    reference=p.reference,
    message = p.message )

    db.add(contactquery)
    db.commit()
    db.refresh(contactquery)
    return contactquery


@router.post("/prayerrequest", response_model=prayerrequest)
def create_prayer_request(p: prayerrequest, db: Session = Depends(get_db)):
    import uuid
    prayerrequest = PrayerRequest(
    id = p.id,
    first_name = p.first_name,
    last_name = p.last_name,
    email=p.email,
    phone_number =p.phone_number,
    address = p.address,
    country =p.country,
    message = p.message )

    db.add(prayerrequest)
    db.commit()
    db.refresh(prayerrequest)
    return prayerrequest

#@router.put("/person/{id}", response_model=person)
#def update_person(id: int, p: person, db: Session = Depends(get_db)):
 #   book_obj = db.query(person).get(id)
  #  book_obj = p.amount
  #  book_obj = p.message
   # db.add(book_obj)
   # db.commit()
   # db.refresh(book_obj)
   # return book_obj


#@router.delete("/person/{id}")
#def delete_person(id: int, db: Session = Depends(get_db)):
#    book_obj = db.query(Personinfo).get(id)
 #   db.delete(book_obj)
  #  db.commit()
   # return "Item was deleted"

