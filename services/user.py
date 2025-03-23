from schema.users_sch import users_schema
from sqlmodel import Session, select
from models.User import User

def get_all_users(db:Session):
    sql_read = select(User)
    users = db.execute(sql_read),all()
    return users_schema

def add_new_user(name: str, email: str, db:Session):
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"mensaje": "Created user successfully"}

def update_user(id: int, name:str, db:Session):
        statement = select(User).where(User.id == id)
        user_db= db.exec(statement).one()
        ##print("Usuario: ", user) --esto no

        user_db.email = name
        db.add(user_db)
        db.commit()
        return {"mensaje": "Update sucessfully"}

def delete_user(id:int, db:Session):
    statement = select(User).where(User.id == id)
    user_db= db.exec(statement).one()

    db.delete(user_db)
    db.commit()
    return {"mensaje": "User deleted successfully"}
