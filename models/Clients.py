from sqlmodel import SQLModel, Field

class Client(SQLModel, table = True):
    dni: int = Field(default=None, primary_key=True)
    nom: str
    email: str
    residencia: str