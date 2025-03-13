from schema.users_sch import users_schema
from sqlmodel import Session, select
from models.User import User

def add_new_user(name: str, email: str, db:Session):
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"mensaje": "Created user successfully"}