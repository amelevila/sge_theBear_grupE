from typing import List
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import read, user, cost, client, producte, reunio, lloc, punt_de_venda
from datetime import date

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
async def update_email_user(uid: int, email: str, db:Session = Depends(get_db)):
    result = user.update_user_email(uid, email, db)
    return result

@app.delete("/user/delete/", response_model=dict)
async def del_user(uid: int, db:Session = Depends(get_db)):
    result = user.delete_user(uid, db)
    return result

#cost
@app.get("/costos/", response_model= list[dict])
def read_cost(db:Session = Depends(get_db)):
    result = cost.llegir_costos(db)
    return result

@app.post("/costos/", response_model=dict)
def create_cost(nom_client: str, comercial: str, venciment: date, nom_producte: str, db:Session = Depends(get_db)):
    result = cost.afegir_cost(nom_client, comercial, venciment, nom_producte, db)
    return result

@app.put("/update_cost/", response_model= dict)
async def update_comercial_cost(numero: int, comercial: str, db:Session = Depends(get_db)):
    result = cost.update_cost_comercial(numero, comercial, db)
    return result

@app.delete("/cost/delete/", response_model=dict)
async def del_cost(numero: int, db:Session = Depends(get_db)):
    result = cost.delete_cost(numero, db)
    return result

#client
@app.get("/clients/", response_model= list[dict])
def read_client(db:Session = Depends(get_db)):
    result = client.llegir_clients(db)
    return result

@app.post("/clients/", response_model=dict)
def create_client(nom: str, email: str, residencia: str, db:Session = Depends(get_db)):
    result = client.afegir_client(nom, email, residencia, db)
    return result

@app.put("/update_client/", response_model= dict)
async def update_email_client(nom: str, email: str, db:Session = Depends(get_db)):
    result = client.update_client_email(nom, email, db)
    return result

@app.delete("/client/delete/", response_model=dict)
async def del_client(nom: str, db:Session = Depends(get_db)):
    result = client.delete_client(nom, db)
    return result

#producte
@app.get("/productes/", response_model= list[dict])
def read_producte(db:Session = Depends(get_db)):
    result = producte.llegir_productes(db)
    return result

@app.post("/productes/", response_model=dict)
def create_producte(nom: str, preu: int, valoracio: int, db:Session = Depends(get_db)):
    result = producte.afegir_producte(nom, preu, valoracio, db)
    return result

@app.put("/update_producte/", response_model= dict)
async def update_preu_producte(nom: str, preu: int, db:Session = Depends(get_db)):
    result = producte.update_producte_preu(nom, preu, db)
    return result

@app.delete("/producte/delete/", response_model=dict)
async def del_producte(nom: str, db:Session = Depends(get_db)):
    result = producte.delete_producte(nom, db)
    return result

#reunio
@app.get("/reunions/", response_model= list[dict])
def read_reunio(db:Session = Depends(get_db)):
    result = reunio.llegir_reunions(db)
    return result

@app.post("/reunions/", response_model=dict)
def create_reunio(assumpte: str, organitzador: str, privacitat: str, data_inici: date, duracio: int, ubicacio: str, url: str, descripcio: str, db:Session = Depends(get_db)):
    result = reunio.afegir_reunio(assumpte, organitzador, privacitat, data_inici, duracio, ubicacio, url, descripcio, db)
    return result

@app.put("/update_reunio/", response_model= dict)
async def update_duracio_reunio(assumpte: str, duracio: int, db:Session = Depends(get_db)):
    result = reunio.update_reunio_duracio(assumpte, duracio, db)
    return result

@app.delete("/reunio/delete/", response_model=dict)
async def del_reunio(assumpte: str, db:Session = Depends(get_db)):
    result = reunio.delete_reunio(assumpte, db)
    return result

#Lloc

@app.get("/lloc/", response_model = list[dict])
def read_lloc(db: Session = Depends(get_db)):
    result = lloc.llegir_lloc(db)
    return result

@app.post("/lloc/", response_model=dict)
def create_lloc(id:int, num_taula: int, lliure:bool, db:Session = Depends(get_db)):
    result = lloc.afegir_lloc(id, num_taula, lliure, db)
    return result

@app.put("/update_lloc/", response_model=dict)
async def update_lliure_lloc(num_taula: int, lliure: bool, db: Session = Depends(get_db)):
    result = lloc.update_lloc_lliure(num_taula, lliure, db)
    return result

@app.delete("/lloc/delete/", response_model=dict)
async def del_lloc(num_taula: int, db: Session = Depends(get_db)):
    result = lloc.delete_lloc(num_taula, db)
    return result

# Punts de venda

@app.get("/punt_de_venda/", response_model=dict[list])
def read_punt_de_venda(db:Session = Depends(get_db)):
    result = punt_de_venda.llegir_punts_de_venda(db)
    return result

@app.post("/punt_de_venda/", response_model=list)
def create_punt_de_venda(lloc:str, calendari:date, venta:str, db:Session = Depends(get_db)):
    result = punt_de_venda.afegir_punts_de_venda(lloc, calendari, venta, db)
    return result

@app.put("/update_punt_de_venda/", response_model=list)
async def update_venda_punt_de_venda(lloc: str, venda: str, db:Session = Depends(get_db)):
    result = punt_de_venda.update_punt_de_venda_venda(lloc, venda, db)
    return result

@app.put("/update_punt_de_venda/", response_model=list)
async def update_lloc_punt_de_venda(lloc: str, venda: str, db:Session = Depends(get_db)):
    result = punt_de_venda.update_punt_de_venda_lloc(lloc, venda, db)
    return result

@app.delete("/punt_de_venda/delete/", response_model=dict)
async def del_punt_de_venda(lloc:str, db:Session = Depends(get_db)):
    return punt_de_venda.delete_punt_de_venda(lloc, db)