from sqlmodel import SQLModel, Field

class Comunicacio(SQLModel, table=True):
    plantilla: str = Field(default=None, primary_key=True)
    unitat: int
    activacio: str
