from fastapi import APIRouter, Depends
from typing import List
from schemas.schemas import  contactquery, donation, prayerrequest, livestreamurl
from models.model import ContactQuery, Donation, PrayerRequest, LiveStreamUrl
from sqlalchemy.orm import Session
from init_db import get_db

router = APIRouter()

#@router.get("/personifo", response_model=List[person])
#async def get_all_persons(db: Session = Depends(get_db)):
#    person = db.query(Personinfo).all()
#    return person

@router.get("/livestreamurl", response_model=List[livestreamurl])
async def get_all_livestream_urls(db: Session = Depends(get_db)):
    livestream_urls = db.query(LiveStreamUrl).all()
    return livestream_urls


@router.post("/contactquery", response_model=contactquery)
def create_contact_query(p: dict, db: Session = Depends(get_db)):
    contactquery = ContactQuery(**p)

    db.add(contactquery)
    db.commit()
    db.refresh(contactquery)
    return contactquery

@router.post("/donation", response_model=donation)
def create_donation(p: dict, db: Session = Depends(get_db)):
    donation = Donation(**p)

    db.add(donation)
    db.commit()
    db.refresh(donation)
    return donation


@router.post("/prayerrequest", response_model=prayerrequest)
def create_prayer_request(p: dict, db: Session = Depends(get_db)):
    print(p)
    prayerrequest = PrayerRequest(**p)
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

