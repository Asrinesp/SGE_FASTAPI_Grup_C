from typing import List
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

from starlette.middleware.cors import CORSMiddleware

#Mis archivos
from services.Factura_srv import get_all_facts, add_factura, delete_factura, update_factura

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

@app.get("/root", response_model=List[dict])
async def read_root():
    return {"message": "API de Facturas funcionando"}

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
