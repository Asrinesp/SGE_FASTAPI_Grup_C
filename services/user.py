from schema.users_sch import users_schema
from sqlmodel import Session, select
from models.User import User

def get_all_users(db:Session):
    sql_read = select(User)
    users = db.exec(sql_read).all()
    return users_schema

def add_new_user(name: str, email:str, db:Session):
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"Message":"User created successfully"}

def update_a_user(db:Session):
    statement = select(User).where(User.id == 1)
    result = db.exec(statement)
    user = result.one()
    print("User:", user)

    user.name = "Ehe"
    db.add(user)
    db.commit()
    return {"Message":"Updated successfully"}

def delete_a_user(db:Session):
    statement = select(User).where(User.id == 1)
    result = db.exec(statement)
    user = result.one()
    print("User: ", user)
    db.delete(user)
    return {"Message":"User deleted successfully"}