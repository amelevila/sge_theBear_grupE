from sqlmodel import SQLModel, Field

class Client(SQLModel, table=True):
    nom: str = Field(default=None, primary_key=True)
    email: str
    residencia: str