from sqlmodel import SQLModel, Field

class Producte(SQLModel, table=True):
    nom: str = Field(default=None, primary_key=True)
    preu: int
    valoracio: int