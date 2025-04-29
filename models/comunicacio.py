from sqlmodel import SQLModel, Field

class comunicacio(SQLModel, table=True):
    plantilla: str = Field(default=None, primary_key=True)
    unitat: int
    activacio: str
