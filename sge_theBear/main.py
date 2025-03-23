from typing import List
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import read
from services import user
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

@app.get("/root", response_model=list[dict])
async def read_root():
    result = read.registre()
    return result

@app.get("/users/", response_model=list[dict])
def read_user(db: Session = Depends(get_db)):
    result = user.get_all_user(db)
    return result

@app.post("/users/", response_model=dict)
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    result = user.add_new_user(name, email, db)
    return result

#Llamamos a la función para actualizar y usamos endpoint para indicar si hacemos post,get,etc.
@app.put("/update_user/", response_model= dict)
#Actualizamos el id,name
async def update_user(id:int,name:str,db:Session = Depends(get_db)):
    #Añadimos el usuario
    result = user,update_user(id, name, db)
    #Ensemao el usultado cambiado
    return result

#Llamamos a la función para eliminar
@app. delete("/user/delete/", response_model=dict)
#Eliminar con el ID
async def delete_user(id:int, db:Session = Depends(get_db)):
    #Se debe poner el ID para eliminar
    result = user.delete_user (id, db)
    return result

