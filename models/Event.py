from sqlmodel import SQLModel, Field
from datetime import date

class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nou_event: str
    reservat: str
    enunciat: str
    informe: str
    data: date