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