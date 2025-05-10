from sqlmodel import SQLModel, Field

class Producte_compra(SQLModel, table=True):
    nom: str = Field(default=None, primary_key=True)
    tipus: str
    preu: int
    categoria: str
