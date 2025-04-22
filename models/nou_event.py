from sqlmodel import SQLModel, Field
from datetime import date

class nouEvent(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    data: date
    entrada: str
    comunicacio: str
    preguntes: str
    notes: str
