from datetime import date
from sqlmodel import SQLModel, Field

class Punt_de_venda(SQLModel, table=True):
    lloc: str = Field(default=None, primary_key=True)
    calendari: date
    venta: str