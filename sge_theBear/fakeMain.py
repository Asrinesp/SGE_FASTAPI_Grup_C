from typing import List
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

# Importar servicios
from services.client import get_all_clients, add_client, update_client, delete_client
from services.menu import get_all_menu_items, add_menu_item, update_menu_item, delete_menu_item

# Importar modelos
from models.client import Client
from models.menu import Menu

app = FastAPI()

# Configuración de la base de datos
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# Crear tablas
SQLModel.metadata.create_all(engine)

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

# Rutas para Client
@app.get("/clients", response_model=List[dict])
async def read_clients(db: Session = Depends(get_db)):
    result = get_all_clients(db)
    return result

@app.post("/clients", response_model=dict)
def create_client(cliente: str, fecha_y_hora: str, db: Session = Depends(get_db)):
    result = add_client(cliente, fecha_y_hora, db)
    return result

@app.put("/clients/{client_id}", response_model=dict)
def modify_client(client_id: int, cliente: str, fecha_y_hora: str, db: Session = Depends(get_db)):
    result = update_client(client_id, cliente, fecha_y_hora, db)
    return result

@app.delete("/clients/{client_id}", response_model=dict)
def remove_client(client_id: int, db: Session = Depends(get_db)):
    result = delete_client(client_id, db)
    return result

# Rutas para Menu
@app.get("/menu", response_model=List[dict])
async def read_menu_items(db: Session = Depends(get_db)):
    result = get_all_menu_items(db)
    return result

@app.post("/menu", response_model=dict)
def create_menu_item(producte: str, precio: int, fecha_y_hora: str, db: Session = Depends(get_db)):
    result = add_menu_item(producte, precio, fecha_y_hora, db)
    return result

@app.put("/menu/{item_id}", response_model=dict)
def modify_menu_item(item_id: int, producte: str, precio: int, fecha_y_hora: str, db: Session = Depends(get_db)):
    result = update_menu_item(item_id, producte, precio, fecha_y_hora, db)
    return result

@app.delete("/menu/{item_id}", response_model=dict)
def remove_menu_item(item_id: int, db: Session = Depends(get_db)):
    result = delete_menu_item(item_id, db)
    return result

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de The Bear"}