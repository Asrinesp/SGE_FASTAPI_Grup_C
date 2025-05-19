from schema.factura_sch import fact_schemas
from sqlmodel import Session, select
from models.Factura import Factura

# Para leer todas las facturas
def get_all_facts(db:Session):
    sql_read = select(Factura)
    factura = db.exec(sql_read).all()
    return fact_schemas(factura)

def add_factura(db: Session, id_factura: int, id_menu: int, id_puntVenta: int, id_cliente: int, data: str, preu_total:int):
    new_factura = Factura(id_factura=id_factura, id_menu = id_menu, id_puntVenta= id_puntVenta, id_cliente= id_cliente, data= data, preu_total= preu_total)
    db.add(new_factura)
    db.commit()
    db.refresh(new_factura)
    return {"message": "Created bill succesfully"}

def delete_factura(db: Session, id_fact: int):
    factura = db.exec(select(Factura).where(Factura.id_factura == id_fact)).first()

    if factura:
        db.delete(factura)
        db.commit()
        return {"message": "Delete bill succesfully"}
    return {"message": "Bill not found"}

def update_factura(
    db: Session,
    id_factura: int,
    id_menu: int,
    id_puntVenta: int,
    id_cliente: int,
    data: str,
    preu_total: int):
    factura = db.exec(
        select(Factura).where(Factura.id_factura == id_factura)
    ).first()
    if not factura:
        return {"message": "Bill not found"}

    factura.id_menu = id_menu
    factura.id_puntVenta = id_puntVenta
    factura.id_cliente = id_cliente
    factura.data = data
    factura.preu_total = preu_total

    db.commit()
    db.refresh(factura)
    return {"message": "Bill updated successfully"}