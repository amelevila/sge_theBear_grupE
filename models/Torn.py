from sqlmodel import SQLModel, Field
from datetime import date

class Torn(SQLModel, table=True):
    nom: str = Field(default=None, primary_key=True)
    recurs: str
    data: date
    minuts: int
