from typing import List
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import read, user
from models import user
import os

# Cargar variables de entorno
load_dotenv()

# Configuración de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# Crear las tablas en la base de datos
SQLModel.metadata.create_all(engine)

# Función para obtener la sesión de la base de datos
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

# Inicializar la aplicación FastAPI
app = FastAPI()

@app.get("/root", response_model=List[dict])
async def read_root():
    result = read.registre()
    return result

@app.post("/users/", response_model=dict)
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    result = user.add_new_user(name, email, db)
    return result

@app.put("/users/", response_model=dict)
def update_heroes(db: Session = Depends(get_db)):
    result = user.update_heroes(db)
    return result