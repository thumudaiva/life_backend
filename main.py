from fastapi import FastAPI
from api import personinfo
from init_db import Base, db_engine 
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
        "*",
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.include_router(personinfo.router, prefix="/api", tags=["Person"])

Base.metadata.create_all(bind=db_engine)

@app.get("/")
async def root():
    return {"status": "OK"}
