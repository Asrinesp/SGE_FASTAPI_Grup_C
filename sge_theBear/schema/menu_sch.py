def menu_schema(menu_item) -> dict:
    send_menu = {
        "ID_compra": menu_item["ID_compra"],
        "Producte": menu_item["Producte"],
        "Precio": menu_item["Precio"],
        "Fecha_y_hora": menu_item["Fecha_y_hora"]
    }
    return send_menu

def menus_schema(menu_items) -> list[dict]:
    return [menu_schema(item) for item in menu_items.values()]