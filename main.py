from typing import List
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

from starlette.middleware.cors import CORSMiddleware

# archivos carlos
from services.Factura_srv import get_all_facts, add_factura, delete_factura, update_factura

# archivos akasha
from services.client import get_all_clients, add_client, update_client, delete_client
from services.menu import get_all_menu_items, add_menu_item, update_menu_item, delete_menu_item
from models.client import Client
from models.menu import Menu

# archivos alvaro
from services.Contiene import get_all_contE, get_one_contE, add_new_puntV, update_contE, delete_contE
from services.PoS import get_one_puntV, get_all_puntVs, add_new_puntV, update_puntV, delete_puntV

app = FastAPI()

# CORS para la tecnologia de frontend

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

SQLModel.metadata.create_all(engine)

# Hace lo mismo que el cursor
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

# ROOT
@app.get("/root", response_model=List[dict])
async def read_root():
    return {"message": "API de Facturas funcionando"}


# PARTE CARLOS
#Leer facturas
@app.get("/facturas/", response_model= list[dict])
async def read_fact(db:Session = Depends(get_db)):
    result = get_all_facts(db)
    return result

# Añadir facturas
@app.post("/facturas/")
async def create_factura(
    id_factura: int,
    id_menu: int,
    id_puntVenta: int,
    id_cliente: int,
    data: str,
    preu_total: int,
    db: Session = Depends(get_db)
):
    result = add_factura(db, id_factura, id_menu, id_puntVenta, id_cliente, data, preu_total)
    return result

# Eliminar factura
@app.delete("/facturas/{id_factura}")
async def remove_factura(id_factura: int, db: Session = Depends(get_db)):
    deleted = delete_factura(db, id_factura)
    return {"deleted": deleted}

# Modificar factura
@app.put("/facturas/{id_factura}")
async def modify_factura(
    id_factura: int,
    id_menu: int,
    id_puntVenta: int,
    id_cliente: int,
    data: str,
    preu_total: int,
    db: Session = Depends(get_db)
):
    return update_factura(db, id_factura, id_menu, id_puntVenta, id_cliente, data, preu_total)

# PARTE AKASHA
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

## ALVARO
@app.get("/puntosV/", response_model=list[dict])
def read_all_puntoV(db: Session = Depends(get_db)):
    result = get_all_puntVs(db)
    return result

##READ ONE
@app.get("/puntV/id/{numero}")
def read_one_puntV(numero: int, db: Session = Depends(get_db)):
    result = get_one_puntV(numero, db)
    return result
###CREAMOS UNO
@app.post("/puntV/", response_model=dict)
def create_puntV(id: int, ubicacion: str, db: Session = Depends(get_db)):
    result = add_new_puntV(id, ubicacion, db)
    return result

##MODIFICAMOS UNO
@app.put("/update_puntV", response_model=dict)
async def update_puntV(id: int, ubicacion: str, db: Session = Depends(get_db)):
    result = update_puntV(id, ubicacion, db)
    return result

##ELIMINAMOS UNO
@app.delete("/PoS/delete/", response_model=dict)
async def delete_puntV(id: int, db: Session = Depends(get_db)):
    result = delete_puntV(id, db)
    return result


# CONTENIR
 ##READ ALL
@app.get("/Contiene/", response_model=List[dict])
def read_all_contE(db: Session = Depends(get_db)):
    result = get_all_contE(db)
    return result

##READ ONE
@app.get("/Contiene/id/{numero}")
def read_one_contE(id_menu: int, db: Session = Depends(get_db)):
    result = get_one_contE(id_menu, db)
    return result

##CREAMOS UNA
@app.post("/Contiene/", response_model=dict)
def create_contE(id_menu: int, id_ingediente: int, db: Session = Depends(get_db)):
    result = add_new_puntV(id_menu, id_ingediente, db)
    return result

##MODIFICAMOS UNO
@app.put("/update_contE", response_model=dict)
async def update_contE(id_menu: int, id_ingrediente: int, db: Session = Depends(get_db)):
    result = update_contE(id_menu, id_ingrediente, db)
    return result

##ELIMINAMOS UNO
@app.delete("/PoS/delete/", response_model=dict)
async def delete_contE(id_menu: int, db: Session = Depends(get_db)):
    result = delete_contE(id_menu, db)
    return result
