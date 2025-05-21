def prove_schema(proveidor) -> dict:
    prove = {
        "cif":proveidor["cif"],
        "nom_fiscal":proveidor["nom_fiscal"]
    }
    return prove

def prove_schemas(proveidors) -> list[dict]:
    return [prove_schema(proveidor) for k,proveidor in proveidors.items()]
