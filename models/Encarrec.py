from sqlmodel import SQLModel, Field
from datetime import date

class Encarrec(SQLModel, table=True):
    nom: str = Field(default=None, primary_key=True)
    proveïdor: str
    data_limit: date
    data_recollida: date
