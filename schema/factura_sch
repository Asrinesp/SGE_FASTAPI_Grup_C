# Transforma la lista de la BBDD a un diccionario
def fact_schema(factura) -> dict:
    fact = {
        "id_factura": factura.id_factura,
        "id_menu": factura.id_menu,
        "id_puntVenta": factura.id_puntVenta,
        "id_cliente": factura.id_cliente,
        "data": factura.data,
        "preu_total": factura.preu_total
    }
    return fact

# Crea una lista de diccionarios con la funcion anterior
def fact_schemas(facturas) -> list[dict]:
    return [fact_schema(factura) for factura in facturas]
