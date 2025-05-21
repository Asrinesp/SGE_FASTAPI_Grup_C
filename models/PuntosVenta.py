'''*******************
Tabla para PuntosVenta
*******************'''

from sqlmodel import SQLModel, Field

class PuntosVenta(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    ubicacion: str