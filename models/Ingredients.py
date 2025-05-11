from sqlmodel import SQLModel, Field

class Ingredients(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nom: str
    id_proveedor: int

