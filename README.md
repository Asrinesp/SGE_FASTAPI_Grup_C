# SGE_FASTAPI_Grup_C

## Yoon López Luis

### PRIMERES PASSES

El primer que hem de fer és crear el sistema d'arxius:

![001.jpg](.img/001.jpg)

És molt important mantenir els arxius `__init__.py` buits.

Posteriorment, afegim el codi al `connect.py`, tal com vam fer a l'activitat anterior.

![002.jpg](.img/002.jpg)

Després, afegim el codi a l'arxiu `read_sch.py`, dins de la carpeta `schema`.

```python
def schema(usr) -> dict:
    send_usr = {"id":usr["id"],
                "name":usr["name"],
                "surname":usr["surname"],
                "age":usr["age"],
                }
    return send_usr

def schemas(users) -> list[dict]:
    return [schema(user) for k,user in users.items()]
```

A continuació, hem d'inserir el codi a `read.py`, dins la carpeta `services`. Aquest arxiu és el que permet treballar amb consultes del client i proporcionar respostes al `main.py`.

```python
from schema import read_sch

def registre():
    users = {
        "user1":{
            "id": 1,
            "name": "Roger",
            "surname": "Sobrino",
            "age": 49
        },
        "user2": {
            "id": 2,
            "name": "Josep Oriol",
            "surname": "Roca",
            "age": 23
        },
        "user3": {
            "id": 3,
            "name": "Juan Manuel",
            "surname": "Sanchez",
            "age": 40
        }
    }

    return read_sch.schemas(users)
```

L'últim arxiu al que li hem de posar codi és el `main.py`, a l'arrel del projecte. Aquest arxiu serà el que controlarà el programa, segons la consulta rebuda.
```python
from typing import List
from fastapi import FastAPI
from services import read

app = FastAPI()

@app.get("/root", response_model=List[dict])
async def read_root():
    result = read.registre()
    return result
```

Quan hem comprovat que tot estigui correcte, hem de posar la següent comanda al terminal, des de l'arrel del projecte:

```commandline
uvicorn main:app --reload
```

En executar-lo, al terminal sortirà el que nosaltres veiem al FastAPI, incloent els errors i a on es troba cadascun.

![003.jpg](.img/003.jpg)

Fins que no es tanqui el FastAPI, no es tancarà l'execució del terminal.

### FASTAPI + DB

#### Instal·lació de requeriments

Abans de continuar, hem d'instal·lar els paquets que requeriràn els codis que farem.

Per fer-ho, hem de crear un arxiu, anomenat `requeriments.txt` i afegirem el nom dels paquets que necessitem.

```text
fastapi
sqlmodel
psycopg2
python-dotenv
uvicorn
```

I ho instal·lem tot a través d'aquest arxiu.

```commandline
pip install -r requeriments.txt
```

Si dona error, hem de canviar `psycopg2` per `psycopg2-binary`

#### Creació del fitxer .env

El fitxer .env és una configuració del projecte per connectar amb la base de dades creada a l'arrel del projecte.

El fitxer ha de tenir el següent codi:

```.env
DATABASE_URL=postgresql+psycopg2://usuari:contrasenya@localhost:5432/the_bear
```

El que fem es desar les variables de l'entorn amb la URL indicat al codi.

`DATABASE_URL`: és el que desa la informació per connectar a la base de dades
- `postgresql+psycopg2`: utilitzarà PostgreSQL a través de psycopg2
- `usuari:contrasenya`: credencials d'accés a la base de dades. Les podem veure a l'arxiu .yml del docker.
- `localhost:5432`: adreça (en aquest cas el propi PC de l'usuari) i el port d'execució de PostgreSQL
- `the_bear`: nom de la base de dades

#### Configuració de SQLModel i PostgreSQL

Al `main.py` hem d'afegir els imports necessaris.

```python
from fastapi import FastAPI,Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import user
import os
```
- `SQLModel`: defineix models de dades i interactua amb la base de dades.
- `create_engine`: crea una connexió amb la base de dades
- `Session`: gestiona les sessions amb la base de dades
- `User`: estableix el model de l'usuari
- `FastAPI`: crea l'aplicació web
- `load_dotenv`: carrega variables d'entorn a través de l'arxiu .env
- `os`: accedeix a les variables de l'entorn.

Al final del codi del `main.py`, afegim:

```python
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

SQLModel.metadata.create_all(engine)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()
```
- `load_dotenv()`: carrega les variables d'entorn segons l'arxiu .env.
- `DATABASE_URL = os.getenv("DATABASEURL")`: obté l'enllaç de la connexió de la base de dades de les variables d'entorn.
- `engine = create_engine(DATABASE_URL)`: crea un objecte per gestionar la connexió de la base de dades, anomenat engine.
- `SQLModel.metadata.create_all(engine)`: Crea la base de dades automàticament a través de engine
- `get_db`: retorna la sessió de la base de dades; `yield db` proporciona la sessió i `db.close()` tanca la sessió quan ja s'ha utilitzat.

#### Definició del Model d’usuaris amb SQLModel
Creem una carpeta, anomenada models, per poder treballar amb el model que establirà la connexió entre la classe `models` i la base de dades, per poder crear la taula corresponent a la base de dades segons l'estructura que haguem definit.

A aquesta carpeta, hem de crear un arxiu anomenat `__init__.py`, que quedarà buit, i `User.py`, on inserirem el codi.

```python
from sqlmodel import SQLModel, Field

class User (SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    email: str
```
- `Field`: serveix per especificar configuracions als diferents caps.

#### Modificació / creació dels endpoints

Hem d'afegir, al final del `main.py`, un nou endpoint que cridi al mètode que fa la consulta a la base de dades i rep la resposta: els usuaris en json.

```python
@app.get("/users", response_model=list[dict])
def read_user(db:Session = Depends(get_db)):
    result = user.get_all_users(db)
    return result
```

Creem un arxiu anomenat `user.py` dins de `services` i afegim el codi:

```python
from schema.users_sch import users_schema
from sqlmodel import Session, select
from models.User import User

def get_all_users(db:Session):
    sql_read = select(User)
    users = db.exec(sql_read).all()
    return users_schema
```
- `db:Session` desa a la base de dades la sessió de la connexió.
- `select`: consulta de sql
- `db.exec`: executa la base de dades

El resultat final, entrant a `127.0.0.1:8000/docs` hauria de ser que, en posar la següent consulta:

![004.jpg](.img/004.jpg)

Doni la següent resposta:

![005.jpg](.img/005.jpg)
![006.jpg](.img/006.jpg)

### CRUD taula user