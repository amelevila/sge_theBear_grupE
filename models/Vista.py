from sqlmodel import SQLModel, Field
from datetime import date

class Vista(SQLModel, table=True):
    nom: str = Field(default=None, primary_key=True)
    data: date
