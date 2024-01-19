from fastapi import FastAPI
from api import personinfo
from init_db import Base, db_engine 
app = FastAPI()


app.include_router(personinfo.router, tags=["Person"])

Base.metadata.create_all(bind=db_engine)

@app.get("/")
async def root():
    return {"status": "OK"}
