from typing import List
from fastapi import FastAPI, Depends
from services import read, user
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

app = FastAPI()

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

SQLModel.metadata.create_all(engine)

# Hace lo que hacia le cursor
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

@app.get("/root", response_model=List[dict])
async def read_root():
    result = read.registre()
    return result

#Para leer los usuarios
@app.get("/read_users/", response_model= list[dict])
async def read_user(db:Session = Depends(get_db)):
    result = user.get_all_users(db)
    return result

#Para añadir usuarios
@app.post("/add_users/", response_model=dict)
async def create_user(name: str, email:str, db:Session = Depends(get_db)):
    result = user.add_new_user(name, email, db)
    return result
