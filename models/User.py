from sqlmodel import SQLModel, Field
from schema.users_sch import users_schema
from sqlmodel import Session, select
from models.User import User

class User(SQLModel, table = True):
    id: int = Field(default=None, primary_key=True)
    name: str
    email: str

def get_all_users(db:Session):
    sql_read = select(User)
    users = db.exec(sql_read).all()
    return users_schema(users)
def add_new_user(name: str, email: str, db: Session):
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"Created user succesfully"}