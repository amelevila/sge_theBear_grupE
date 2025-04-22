from sqlmodel import SQLModel, Field

class Lloc(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    num_taula: int
    lliure: bool

