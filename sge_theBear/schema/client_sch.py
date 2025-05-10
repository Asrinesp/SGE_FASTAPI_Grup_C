def client_schema(client) -> dict:
    send_client = {
        "ID_citas": client["ID_citas"],
        "Cliente": client["Cliente"],
        "Fecha_y_hora": client["Fecha_y_hora"]
    }
    return send_client

def schemas(clients) -> list[dict]:
    return [client_schema(client) for client in clients.values()]