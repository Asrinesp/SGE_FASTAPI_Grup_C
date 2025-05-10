from email.policy import default
from sqlmodel import SQLModel, Field

class Menu(SQLModel, table=True):
    ID_compra : int = Field(default=None, primary_key=True)
    Producte : str
    Precio : int
    Fecha_y_hora : str


