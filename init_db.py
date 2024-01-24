import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


SQLALCHEMY_DATABASE_URL = 'mysql://lifeadmin:LifeAdmin123@biblemission.ckxpycyjiukv.ap-south-1.rds.amazonaws.com/lifedb'
#f'mysql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}/{os.getenv("DB_NAME")}'




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
