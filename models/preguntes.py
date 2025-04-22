from sqlmodel import SQLModel, Field

class preguntes(SQLModel, table=True):
    titol: str = Field(default=None, primary_key=True)
    tipus: str
