from typing import List
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import read, user
import os

app = FastAPI()

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

@app.get("/root", response_model=List[dict])
async def read_root():
    result = read.registre()
    return result

#user
@app.get("/users/", response_model= list[dict])
def read_user(db:Session = Depends(get_db)):
    result = user.get_all_users(db)
    return result

@app.post("/users/", response_model=dict)
def create_user(name: str, email:str, db:Session = Depends(get_db)):
    result = user.add_new_user(name, email, db)
    return result

@app.put("/update_user/", response_model= dict)
async def update_email(uid: int, email: str, db:Session = Depends(get_db)):
    result = user.update_user_email(uid, email, db)
    return result

@app.delete("/user/delete/", response_model=dict)
async def del_user(uid: int, db:Session = Depends(get_db)):
    result = user.delete_user(uid, db)
    return result

#user
@app.get("/users/", response_model= list[dict])
def read_user(db:Session = Depends(get_db)):
    result = user.get_all_users(db)
    return result

@app.post("/users/", response_model=dict)
def create_user(name: str, email:str, db:Session = Depends(get_db)):
    result = user.add_new_user(name, email, db)
    return result

@app.put("/update_user/", response_model= dict)
async def update_email(uid: int, email: str, db:Session = Depends(get_db)):
    result = user.update_user_email(uid, email, db)
    return result

@app.delete("/user/delete/", response_model=dict)
async def del_user(uid: int, db:Session = Depends(get_db)):
    result = user.delete_user(uid, db)
    return result