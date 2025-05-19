from typing import List
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

from starlette.middleware.cors import CORSMiddleware

#Mis archivos
from services.Factura_srv import get_all_facts, add_factura, delete_factura, update_factura
from services.Ingredientes_srv import get_all_ingredients, add_ingredient, delete_ingredient, update_ingredient
from services.Proveidor_srv import get_all_proveidors, add_proveidor, delete_proveidor, update_proveidor

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

# El base model
class FacturaCreate(BaseModel):
    id_factura: int
    id_menu: int
    id_puntVenta: int
    id_cliente: int
    data: str
    preu_total: int


@app.get("/root", response_model=List[dict])
async def read_root():
    return {"message": "API de Facturas funcionando"}

# ----------------------------- FACTURAS -----------------------------

#Leer facturas
@app.get("/facturas/", response_model= list[dict])
async def read_fact(db:Session = Depends(get_db)):
    result = get_all_facts(db)
    return result

# Añadir facturas
@app.post("/facturas/crear/")
async def create_factura(
        factura: FacturaCreate,
        db: Session = Depends(get_db)
):
    result = add_factura(
        db,
        factura.id_factura,
        factura.id_menu,
        factura.id_puntVenta,
        factura.id_cliente,
        factura.data,
        factura.preu_total
    )
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

# ----------------------------- INGREDIENTES -----------------------------
@app.get("/ingredientes/", response_model=List[dict])
async def read_ingredients(db: Session = Depends(get_db)):
    return get_all_ingredients(db)

@app.post("/ingredientes/crear/")
async def create_ingredient(
    id: int,
    nom: str,
    id_proveedor: int,
    db: Session = Depends(get_db)
):
    return add_ingredient(db, id, nom, id_proveedor)

@app.delete("/ingredientes/{id}")
async def remove_ingredient(id: int, db: Session = Depends(get_db)):
    return delete_ingredient(db, id)

@app.put("/ingredientes/{id}")
async def modify_ingredient(
    id: int,
    nom: str,
    id_proveedor: int,
    db: Session = Depends(get_db)
):
    return update_ingredient(db, id, nom, id_proveedor)

# ----------------------------- PROVEEDORES -----------------------------
async def read_proveidors(db: Session = Depends(get_db)):
    return get_all_proveidors(db)

@app.post("/proveidors/crear/")
async def create_proveidor(
    cif: str,
    nom_fiscal: str,
    db: Session = Depends(get_db)
):
    return add_proveidor(db, cif, nom_fiscal)

@app.delete("/proveidors/{cif}")
async def remove_proveidor(cif: str, db: Session = Depends(get_db)):
    return delete_proveidor(db, cif)

@app.put("/proveidors/{cif}")
async def modify_proveidor(
    cif: str,
    nom_fiscal: str,
    db: Session = Depends(get_db)
):
    return update_proveidor(db, cif, nom_fiscal)
