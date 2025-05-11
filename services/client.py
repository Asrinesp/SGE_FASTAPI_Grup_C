from schema.client_sch import client_schema, clients_schema
from models.client import Client
from sqlmodel import Session, select


# Obtener todas las citas de clientes
def get_all_clients(db: Session):
    sql_read = select(Client)
    clients = db.exec(sql_read).all()
    return clients_schema(clients)


# Añadir nueva cita de cliente
def add_client(cliente: str, fecha_y_hora: str, db: Session):
    db_client = Client(Cliente=cliente, Fecha_y_hora=fecha_y_hora)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return {"message": "Cita de cliente añadida exitosamente"}


# Modificar cita de cliente
def update_client(client_id: int, cliente: str, fecha_y_hora: str, db: Session):
    db_client = db.get(Client, client_id)
    if not db_client:
        return {"error": "Cita no encontrada"}

    db_client.Cliente = cliente
    db_client.Fecha_y_hora = fecha_y_hora

    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return {"message": "Cita actualizada exitosamente"}


# Eliminar cita de cliente
def delete_client(client_id: int, db: Session):
    db_client = db.get(Client, client_id)
    if not db_client:
        return {"error": "Cita no encontrada"}

    db.delete(db_client)
    db.commit()
    return {"message": "Cita eliminada exitosamente"}
