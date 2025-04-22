from datetime import date
from sqlmodel import SQLModel, Field

class Cost(SQLModel, table=True):
    numero: int = Field(default=None, primary_key=True)
    nom_client: str
    comercial: str
    venciment: date
    nom_producte: str