from schema.contenir_sch import contenir_schema, contenir_schemas
from sqlmodel import Session, select
from models.Contenir import Contenir

##READ ALL
def get_all_contE(db:Session):
    sql_read = select(Contenir)
    contienE = db.exec(sql_read).all()
    return contenir_schemas(contienE)

##READ ONE
def get_one_contE(id_menu: int, id_ingrediente: int, db:Session):
    sql_read = select(Contenir).where(Contenir.id_menu == id_menu).where(Contenir.id_ingrediente == id_ingrediente)
    result = db.exec(sql_read).first()
    if result is None:
        return {"Relación de Contenido no existe"}

    return contenir_schema(result)

##CREATE ONE
def add_new_puntV(id_menu: int, id_ingrediente: int, db:Session):
    db_pos = Contenir(id_menu=id_menu, id_ingrediente=id_ingrediente)
    db.add(db_pos)
    db.commit()
    db.refresh(db_pos)
    return {"ACIERTO":"Se ha creado una nueva relación de contenido"}

##UPDATE ONE
def update_contE(id_menu: int, id_ingrediente: int, db:Session):
    sql_select = select(Contenir).where(Contenir.id_menu == id_menu).where(Contenir.id_ingrediente == id_ingrediente)
    user_db = db.exec(sql_select).first()
    if user_db is None:
        print(f"*********************************************************",
              f"[AVISO] Se intentó actualizar una relación inexistente: {id}".upper(),
              f"*********************************************************")

        return {"ERROR":"Punto de Venta no existe"}
    user_db.id_menu = id_menu
    user_db.id_ingrediente = id_ingrediente
    db.add(user_db)
    db.commit()
    return {"Relación de Contenido" : "Actualizada Correctamente"}

##DELETE ONE
def delete_contE(id_menu: int, id_ingrediente: int, db:Session):
    sql_select = select(Contenir).where(Contenir.id_menu == id_menu).where(Contenir.id_ingrediente == id_ingrediente)
    user_db= db.exec(sql_select).first()
    if user_db is None:
        print(f"*********************************************************",
              f"[AVISO] Se intentó eliminar un id inexistente con id: {id}".upper(),
              f"*********************************************************")

        return {"ERROR":"Punto de Venta no existe"}
    db.delete(user_db)
    db.commit()
    return {"Punto de Venta" : "Eliminado Correctamente"}