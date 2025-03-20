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

def update_user(db:Session):
        statement = select(User).where(User.id == "1")
        results = db.execute(statement)
        user = results.one()
        print("Usuario: ", user)

        user.email = "carlosdondeestas@itic.cat"
        db.add(user)
        db.commit()
        return {"mensaje": user}

def delete_user(db:Session):
    statement = select(User).where(User.id == "1")
    results = db.execute(statement)
    user = results.one()
    print("User: ", user)
    db.delete(user)
    db.commit()
