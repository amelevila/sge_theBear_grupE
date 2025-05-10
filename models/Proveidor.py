from sqlmodel import SQLModel, Field

class Proveidor(SQLModel, table=True):
    nom: str = Field(default=None, primary_key=True)
    correu_electronic: str
    direccio: str
    telefon: str
