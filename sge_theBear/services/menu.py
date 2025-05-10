from ..schema.menu_sch import menu_schema, menus_schema
from sqlmodel import Session, select
from ..models.menu import Menu


# Obtener todos los items del menú
def get_all_menu_items(db: Session):
    sql_read = select(Menu)
    menu_items = db.exec(sql_read).all()
    return menus_schema(menu_items)


# Añadir nuevo item al menú
def add_menu_item(producte: str, precio: int, fecha_y_hora: str, db: Session):
    db_item = Menu(Producte=producte, Precio=precio, Fecha_y_hora=fecha_y_hora)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"message": "Item añadido al menú exitosamente"}


# Modificar item del menú
def update_menu_item(item_id: int, producte: str, precio: int, fecha_y_hora: str, db: Session):
    db_item = db.get(Menu, item_id)
    if not db_item:
        return {"error": "Item no encontrado"}

    db_item.Producte = producte
    db_item.Precio = precio
    db_item.Fecha_y_hora = fecha_y_hora

    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"message": "Item actualizado exitosamente"}


# Eliminar item del menú
def delete_menu_item(item_id: int, db: Session):
    db_item = db.get(Menu, item_id)
    if not db_item:
        return {"error": "Item no encontrado"}

    db.delete(db_item)
    db.commit()
    return {"message": "Item eliminado exitosamente"}