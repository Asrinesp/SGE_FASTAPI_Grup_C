from sqlmodel import SQLModel, Field

class Factura(SQLModel, table=True):
    id_factura: int = Field(default=None, primary_key=True)
    id_menu: int = Field(default=None, primary_key=True)
    id_puntVenta: int = Field(default=None, primary_key=True)
    id_cliente: int
    data: str
    preu_total: int

