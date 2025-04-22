from sqlmodel import SQLModel, Field
from datetime import date, time

class Reunio(SQLModel, table=True):
    assumpte: str = Field(default=None, primary_key=True)
    organitzador: str
    privacitat: str
    data_inici: date
    duracio: int
    ubicacio: str
    url: str
    descripcio: str
    