from sge_theBear.schema.users_sch import users_schema
from sqlalchemy.sql.functions import session_user
from sqlmodel import Session, select
from models.user import user


def get_all_users(db:Session):
    sql_read = select(user)
    users = db.exec(sql_read).all()
    return users_schema(users)

def add_new_user(name:str,email:str,db:Session):
    db_user = user(name=name,email=email)
    db.add(db_user)
    db.commit()
    db.referesh(db_user)
    return {"Created user succesdfully"}

#Hacemos una función con cualquiera nombre y le pasamos en el parametro
#los tipos de datos que vamos a actualizar
def update_user(id:int, name:str, db:Session):
    #Selecimos los usuarios que tenga ID
    # Los objetos se poder llamar como sea
    sql_select = select(user).where(user.id == id)
    #Ejecumas solo uno
    user_db = db.exec (sql_select).one()
    #Cambios el nombre
    user_db.name = name
    #Lo añadimos al usuario
    db.add(user_db)
    #Hacemos un commit
    db.commit()
    #Retornamos el resultado que se hecho correctament
    return {"msg":"Updated user succesfully"}

#Eliminamos los usuarios segun su id
def delete_user(id:int, db:Session):
    #Buscamos si hay ID en los usuarios
    sql_select = select (User).where(User. id == id)
    #Ejecutamos uno de los usuarios
    user_db = db. exec (sql_select) .one()

    #Eliminamos el usuario
    db. delete(user_db)
    #Hacemos un commit
    db.commit ( )
    #Retornamos el resultado que se hecho correctamente
    return {"msg":"Deleted user succesfully"}
