from sqlmodel import SQLModel, Field
from datetime import date

class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nou_event: str
    reservats: str
    anunciats: str
    informes: str
    data: date