from datetime import date
from sqlmodel import SQLModel

class punts_de_venda(SQLModel, table = True):
    lloc: str
    calendari = date
    venta: str
