def schema(pVto) -> dict:
    send_pVto = { "id":pVto["id"],
                "ubicacion": pVto["ubicacion"]
    }
    return send_pVto

##TRANSFORMAMOS SOLO UNO
def pos_schema(pos) -> dict:
    response = {"Punto de Venta":pos}
    return response

##TRANSFORMAMOS MUCHOS
def pos_schemas(posS)->list[dict]:
    response = [pos_schema(pos) for pos in posS]
    return response