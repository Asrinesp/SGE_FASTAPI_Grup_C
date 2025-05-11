from sqlmodel import SQLModel, Field


class Proveidor(SQLModel, table=True):
    cif: int = Field(default=None, primary_key=True)
    nom_fiscal: str
