# SGE_FASTAPI_Grup_C

## Yoon López Luis

### PRIMERES PASSES

El primer que hem de fer és crear el sistema d'arxius:

![001.jpg](.img/001.jpg)

És molt important mantenir els arxius `__init__.py` buits.

Posteriorment, afegim el codi al `connect.py`, tal com vam fer a l'activitat anterior.

![002.jpg](.img/002.jpg)

Després, afegim el codi a l'arxiu `read_sch.py`, dins de la carpeta `schema`.

```commandline
def schema(usr) -> dict:
    send_usr = {"id":["id"],
                "name":usr["name"],
                "surname":usr["surname"],
                "age":usr["age"],
                }
    return send_usr

def schemas(users) -> list[dict]:
    return [schema(user) for k,user in users.items()]
```