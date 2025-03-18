from typing import List
from fastapi import FastAPI, Depends
from services import read, user
from sqlmodel import SQLModel, create_engine, Session, select
from dotenv import load_dotenv
from models import User
import os

app = FastAPI()

@app.get("/root", response_model=List[dict])
async def read_root():
    result = read.registre()
    return result



load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

SQLModel.metadata.create_all(engine)


def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()


@app.get("/users/", response_model= list[dict])
def read_user(db:Session = Depends(get_db)):
    result = user.get_all_users(db)
    return result

@app.post("/users/", response_model=dict)
def create_user(name: str, email:str, db:Session = Depends(get_db)):
    result = user.add_new_user(name, email, db)
    return result

@app.put("/users/{user_id}")
async def update_user(user_id: int, new_name: str, session: Session = Depends(get_session)):
    statement = select(User).where(User.id == user_id)
    user = session.exec(statement).one_or_none()
    if user is None:
        return {"error": "User not found"}

    user.name = new_name
    session.add(user)
    session.commit()
    return {"message": "User updated", "user": user}

@app.delete("/users/{user_id}")
async def delete_user(user_id: int, session: Session = Depends(get_db)):
    statement = select(User).where(User.id == user_id)
    user = session.exec(statement).one_or_none()
    if user is None:
        return {"error": "User not found"}

    session.delete(user)
    session.commit()
    return {"message": "User deleted"}

