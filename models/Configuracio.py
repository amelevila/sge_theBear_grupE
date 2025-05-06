from sqlmodel import SQLModel, Field
from datetime import date

class Configuracio(SQLModel, table=True):
    plantilla: str = Field(default=None, primary_key=True)
    etapes: date
    etiquetes: str
