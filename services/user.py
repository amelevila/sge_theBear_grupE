from schema.users_sch import users_schema
from sqlmodel import Session, select
from models.User import User

def get_all_users(db:Session):
    sql_read = select(User)
    users = db.exec(sql_read).all()
    return users_schema(users)

def  add_new_user(name: str, email:str, db:Session):
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"Created user successfully"}

def update_user_email(uid: int, email:str, db:Session):
    statement = select(User).where(User.id == uid)
    results = db.exec(statement)
    user = results.one()
    user.email = email
    db.add(user)
    db.commit()
    return {"Email updated successfully"}

def delete_user(uid: int, db:Session):
    statement = select(User).where(User.id == uid)
    results = db.exec(statement)
    user = results.one()
    db.delete(user)
    db.commit()
    return {"User deleted successfully"}
