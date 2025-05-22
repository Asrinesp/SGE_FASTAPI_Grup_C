'''*****************
Tabla de la
relación 'contenir'
*****************'''

from sqlmodel import Field, SQLModel

class Contenir(SQLModel, table = True):
    id_menu: int = Field(primary_key=True)
    id_ingrediente: int = Field(primary_key=True)