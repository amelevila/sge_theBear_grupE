from sqlmodel import SQLModel, Field
from datetime import date

class Entrada(SQLModel, table=True):
    producte: str = Field(default=None, primary_key=True)
    nom: str
    preu: float
    data_ventes: date
    maxim_persones: int
