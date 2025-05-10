from sqlmodel import SQLModel, Field

class Client(SQLModel, table=True):
    ID_citas : int = Field(default=None, primary_key=True)
    Cliente : str
    Fecha_y_hora : str
