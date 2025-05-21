from schema.punV_sch import pos_schemas, pos_schema
from sqlmodel import Session, select
from models.PuntosVenta import PuntosVenta


##READ ALL
def get_all_puntVs(db:Session):
    sql_read = select(PuntosVenta)
    puntVs = db.exec(sql_read).all()
    return pos_schemas(puntVs)

##READ ONE
def get_one_puntV(id: int, db:Session):
    sql_read = select(PuntosVenta).where(PuntosVenta.id == id)
    result = db.exec(sql_read).first()
    if result is None:
        return {"Punto de Venta no existe"}

    return pos_schema(result)

##CREATE ONE
def add_new_puntV(id: int, ubicacion: str, db:Session):
    db_pos = PuntosVenta(id=id, ubicacion=ubicacion)
    db.add(db_pos)
    db.commit()
    db.refresh(db_pos)
    return {"ACIERTO":"Se ha creado un punto de venta"}

##UPDATE ONE
def update_puntV(id: int, ubicacion: str, db:Session):
    sql_select = select(PuntosVenta).where(PuntosVenta.id == id)
    user_db = db.exec(sql_select).first()
    if user_db is None:
        print(f"*********************************************************",
              f"[AVISO] Se intentó actualizar un id inexistente con id: {id}".upper(),
              f"*********************************************************")

        return {"ERROR":"Punto de Venta no existe"}
    user_db.ubicacion = ubicacion
    db.add(user_db)
    db.commit()
    return {"Punto de Venta" : "Actualizado Correctamente"}

##DELETE ONE
def delete_puntV(id: int, db:Session):
    sql_select = select(PuntosVenta).where(PuntosVenta.id == id)
    user_db= db.exec(sql_select).first()
    if user_db is None:
        print(f"*********************************************************",
              f"[AVISO] Se intentó eliminar un id inexistente con id: {id}".upper(),
              f"*********************************************************")

        return {"ERROR":"Punto de Venta no existe"}
    db.delete(user_db)
    db.commit()
    return {"Punto de Venta" : "Eliminado Correctamente"}
