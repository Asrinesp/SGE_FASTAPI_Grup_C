def schema(conT) -> dict:
    send_conT = { "id_menu":conT["id_menu"],
                "id_ingrediente": conT["id_ingrediente"],
    }
    return send_conT

##TRANSFORMAMOS SOLO UNO
def contenir_schema(conT) -> dict:
    response = {"Contiene": conT}
    return response

##TRANSFORMAMOS MUCHOS
def contenir_schemas(conTs) -> list[dict]:
    response = [contenir_schema(conT) for conT in conTs]
    return response