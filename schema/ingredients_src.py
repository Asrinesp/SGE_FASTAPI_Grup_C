def ingre_schema(ingredient) -> dict:
    ingre = {
        "id":ingredient["id"],
        "nom":ingredient["nom"],
        "id_proveedor":ingredient["id_proveedor"]
    }
    return ingre

def ingre_schemas(ingredients) -> list[dict]:
    return [ingre_schema(ingredient) for k,ingredient in ingredients.items()]
