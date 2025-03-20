from schema.users_sch import users_schema
from sqlalchemy.sql.functions import session_user
from sqlmodel import Session, select
from models.user import user

def get_all_users(db:Session):
    sql_read = select(user)
    users = db.exec(sql_read).all()
    return users_schema(users)


def update_heroes(db:Session):
    statement = select(user).where(user.name == "Akasha")
    ActualizarDatos = db.exec(statement).all()
    print(ActualizarDatos)


