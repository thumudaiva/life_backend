import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


SQLALCHEMY_DATABASE_URL ='sqlite:///./users.db'
#f'postgresql+psycopg2://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}/{os.getenv("DB_NAME")}'

db_engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    
    echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)


class Base(DeclarativeBase):
    pass


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
