from sqlmodel import SQLModel, Field

class Empleat(SQLModel, table=True):
    nom: str = Field(default=None, primary_key=True)
    carrec: str
    curriculum: str
    habilitats: str
    telefon: int
    email: str
