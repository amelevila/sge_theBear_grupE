from sqlmodel import SQLModel, Field

class preguntes(SQLModel, table=True):
    nota: str = Field(default=None, primary_key=True)
    instruccions: str
