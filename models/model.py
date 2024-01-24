from init_db import Base
from sqlalchemy import String, BigInteger, FLOAT, INT
from sqlalchemy.orm import mapped_column, Mapped, relationship



class ContactQuery(Base):
    __tablename__ = "contactquery"
    id = mapped_column(BigInteger, primary_key=True)
    first_name = mapped_column(String(100), nullable=False)
    email=mapped_column(String(100), nullable=False)
    phone_number =mapped_column(String(100), nullable=False)
    subject = mapped_column(String(100), nullable=False)
    message = mapped_column(String(250), nullable=True)


class Donation(Base):
    __tablename__ = "donation"
    id = mapped_column(BigInteger, primary_key=True)
    first_name = mapped_column(String(100), nullable=False)
    last_name = mapped_column(String(100), nullable=False)
    email=mapped_column(String(100), nullable=False)
    phone_number =mapped_column(String(100), nullable=False)
    address = mapped_column(String(250), nullable=False)
    country =mapped_column(String(100), nullable=False)
    amount = mapped_column(FLOAT, nullable=False)
    message = mapped_column(String(250), nullable=True)
    reference = mapped_column(String(100), nullable=False)


class PrayerRequest(Base):
    __tablename__ = "prayerrequest"
    id = mapped_column(BigInteger, primary_key=True)
    first_name = mapped_column(String(100), nullable=False)
    last_name = mapped_column(String(100), nullable=False)
    email=mapped_column(String(100), nullable=False)
    phone_number =mapped_column(String(100), nullable=False)
    address = mapped_column(String(250), nullable=False)
    country =mapped_column(String(100), nullable=False)
    message = mapped_column(String(250), nullable=True)

