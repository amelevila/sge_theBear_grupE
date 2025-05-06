from typing import List
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import read, user, cost, client, producte, reunio, empleat, event, entrada, comunicacio
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

#empleat
@app.get("/empleats/", response_model=list[dict])
def read_empleats(db: Session = Depends(get_db)):
    return empleat.llegir_empleats(db)

@app.post("/empleats/", response_model=dict)
def create_empleat(nom: str, carrec: str, curriculum: str, habilitats: str, telefon: int, email: str, db: Session = Depends(get_db)):
    return empleat.afegir_empleat(nom, carrec, curriculum, habilitats, telefon, email, db)

@app.put("/empleats/", response_model=dict)
def update_empleat(nom: str, email: str, db: Session = Depends(get_db)):
    return empleat.update_empleat_email(nom, email, db)

@app.delete("/empleats/", response_model=dict)
def delete_empleat(nom: str, db: Session = Depends(get_db)):
    return empleat.delete_empleat(nom, db)

#event
@app.get("/events/", response_model=list[dict])
def read_events(db: Session = Depends(get_db)):
    return event.llegir_events(db)

@app.post("/events/", response_model=dict)
def create_event(nou_event: str, reservats: str, anunciats: str, informes: str, data: str, db: Session = Depends(get_db)):
    from datetime import datetime
    parsed_date = datetime.strptime(data, "%Y-%m-%d").date()
    return event.afegir_event(nou_event, reservats, anunciats, informes, parsed_date, db)

@app.put("/events/", response_model=dict)
def update_event(event_id: int, nova_data: str, db: Session = Depends(get_db)):
    from datetime import datetime
    parsed_date = datetime.strptime(nova_data, "%Y-%m-%d").date()
    return event.update_event_data(event_id, parsed_date, db)

@app.delete("/events/", response_model=dict)
def delete_event(event_id: int, db: Session = Depends(get_db)):
    return event.delete_event(event_id, db)

#entrada
@app.get("/entrades/", response_model=list[dict])
def read_entrades(db: Session = Depends(get_db)):
    return entrada.llegir_entrades(db)

@app.post("/entrades/", response_model=dict)
def create_entrada(producte: str, nom: str, preu: float, data_ventes: str, maxim_persones: int, db: Session = Depends(get_db)):
    from datetime import datetime
    parsed_date = datetime.strptime(data_ventes, "%Y-%m-%d").date()
    return entrada.afegir_entrada(producte, nom, preu, parsed_date, maxim_persones, db)

@app.put("/entrades/", response_model=dict)
def update_preu(producte: str, nou_preu: float, db: Session = Depends(get_db)):
    return entrada.update_entrada_preu(producte, nou_preu, db)

@app.delete("/entrades/", response_model=dict)
def delete_entrada(producte: str, db: Session = Depends(get_db)):
    return entrada.delete_entrada(producte, db)

#comunicació
@app.get("/comunicacions/", response_model=list[dict])
def read_comunicacions(db: Session = Depends(get_db)):
    return comunicacio.llegir_comunicacions(db)

@app.post("/comunicacions/", response_model=dict)
def create_comunicacio(plantilla: str, unitat: int, activacio: str, db: Session = Depends(get_db)):
    return comunicacio.afegir_comunicacio(plantilla, unitat, activacio, db)

@app.put("/comunicacions/", response_model=dict)
def update_comunicacio(plantilla: str, nova_activacio: str, db: Session = Depends(get_db)):
    return comunicacio.update_comunicacio_activacio(plantilla, nova_activacio, db)

@app.delete("/comunicacions/", response_model=dict)
def delete_comunicacio(plantilla: str, db: Session = Depends(get_db)):
    return comunicacio.delete_comunicacio(plantilla, db)