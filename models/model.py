from init_db import Base
from sqlalchemy import String, BigInteger, FLOAT, INT
from sqlalchemy.orm import mapped_column, Mapped, relationship



class Personinfo(Base):
    __tablename__ = "personinfo"
    id = mapped_column(BigInteger, primary_key=True)
    first_name = mapped_column(String, nullable=False)
    last_name = mapped_column(String, nullable=False)
    email=mapped_column(String, nullable=False)
    phone_number =mapped_column(String, nullable=False)
    address = mapped_column(String, nullable=False)
    country =mapped_column(String, nullable=False)
    amount = mapped_column(FLOAT, nullable=False)
    message = mapped_column(String, nullable=False)


class country(Base):
    __tablename__ = "country"
    
    id  = mapped_column(BigInteger, primary_key=True)
    name = mapped_column(String, nullable=False)