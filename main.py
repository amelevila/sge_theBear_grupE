from typing import List
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import read, user, cost, client, producte, reunio, empleat, event, entrada, comunicacio, lloc, punt_de_venda, encarrec, vista, torn, producte_compra, proveidor
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

#cost
@app.get("/costos/", response_model= list[dict])
def read_cost(db:Session = Depends(get_db)):
    result = cost.llegir_costos(db)
    return result

@app.post("/cost/create/", response_model=dict)
def create_cost(numero: int, nom_client: str, comercial: str, venciment: date, nom_producte: str, db:Session = Depends(get_db)):
    result = cost.afegir_cost(numero, nom_client, comercial, venciment, nom_producte, db)
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

@app.post("/clients/create/", response_model=dict)
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

@app.post("/productes/create/", response_model=dict)
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

@app.post("/reunions/create/", response_model=dict)
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
@app.get("/punt_de_venda/", response_model=list[dict])
def read_punt_de_venda(db:Session = Depends(get_db)):
    result = punt_de_venda.llegir_punts_de_venda(db)
    return result

@app.post("/punt_de_venda/", response_model=dict)
def create_punt_de_venda(lloc:str, calendari:date, venta:str, db:Session = Depends(get_db)):
    result = punt_de_venda.afegir_punts_de_venda(lloc, calendari, venta, db)
    return result

@app.put("/update_punt_de_venda/", response_model=dict)
async def update_lloc_punt_de_venda(lloc: str, venda: str, db:Session = Depends(get_db)):
    result = punt_de_venda.update_punt_de_venda_lloc(lloc, venda, db)
    return result

@app.delete("/punt_de_venda/delete/", response_model=dict)
async def del_punt_de_venda(lloc:str, db:Session = Depends(get_db)):
    return punt_de_venda.delete_punt_de_venda(lloc, db)

#Encarrecs
@app.get("/encarrecs/", response_model=list[dict])
def read_encarrec(db: Session = Depends(get_db)):
    result = encarrec.llegir_encarrecs(db)
    return result

@app.post("/encarrecs/", response_model=dict)
def create_encarrec(nom: str, proveïdor: str, data_limit: date, data_recollida: date, db: Session = Depends(get_db)):
    result = encarrec.afegir_encarrec(nom, proveïdor, data_limit, data_recollida, db)
    return result

@app.put("/update_encarrec/", response_model=dict)
async def update_data_recollida_encarrec(nom: str, data_recollida: date, db: Session = Depends(get_db)):
    result = encarrec.update_encarrec_data_recollida(nom, data_recollida, db)
    return result

@app.delete("/encarrec/delete/", response_model=dict)
async def del_encarrec(nom: str, db: Session = Depends(get_db)):
    result = encarrec.delete_encarrec(nom, db)
    return result

#Vista
@app.get("/vistes/", response_model=list[dict])
def read_vista(db: Session = Depends(get_db)):
    result = vista.llegir_vistes(db)
    return result

@app.post("/vistes/", response_model=dict)
def create_vista(nom: str, data: date, db: Session = Depends(get_db)):
    result = vista.afegir_vista(nom, data, db)
    return result

@app.put("/update_vista/", response_model=dict)
async def update_data_vista(nom: str, data: date, db: Session = Depends(get_db)):
    result = vista.update_vista_data(nom, data, db)
    return result

@app.delete("/vista/delete/", response_model=dict)
async def del_vista(nom: str, db: Session = Depends(get_db)):
    result = vista.delete_vista(nom, db)
    return result

#Torn
@app.get("/torns/", response_model=list[dict])
def read_torn(db: Session = Depends(get_db)):
    result = torn.llegir_torns(db)
    return result

@app.post("/torns/", response_model=dict)
def create_torn(nom: str, recurs: str, data: date, minuts: int, db: Session = Depends(get_db)):
    result = torn.afegir_torn(nom, recurs, data, minuts, db)
    return result

@app.put("/update_torn/", response_model=dict)
async def update_minuts_torn(nom: str, minuts: int, db: Session = Depends(get_db)):
    result = torn.update_torn_minuts(nom, minuts, db)
    return result

@app.delete("/torn/delete/", response_model=dict)
async def del_torn(nom: str, db: Session = Depends(get_db)):
    result = torn.delete_torn(nom, db)
    return result


#Producte_compra
@app.get("/productes_compra/", response_model=list[dict])
def read_producte_compra(db: Session = Depends(get_db)):
    result = producte_compra.llegir_productes_compra(db)
    return result

@app.post("/productes_compra/", response_model=dict)
def create_producte_compra(nom: str, tipus: str, preu: int, categoria: str, db: Session = Depends(get_db)):
    result = producte_compra.afegir_producte_compra(nom, tipus, preu, categoria, db)
    return result

@app.put("/update_producte_compra/", response_model=dict)
async def update_preu_producte_compra(nom: str, preu: int, db: Session = Depends(get_db)):
    result = producte_compra.update_producte_compra_preu(nom, preu, db)
    return result

@app.delete("/producte_compra/delete/", response_model=dict)
async def del_producte_compra(nom: str, db: Session = Depends(get_db)):
    result = producte_compra.delete_producte_compra(nom, db)
    return result

#Proveidor
@app.get("/proveidors/", response_model=list[dict])
def read_proveidor(db: Session = Depends(get_db)):
    result = proveidor.llegir_proveidors(db)
    return result

@app.post("/proveidors/", response_model=dict)
def create_proveidor(nom: str, correu_electronic: str, direccio: str, telefon: str, db: Session = Depends(get_db)):
    result = proveidor.afegir_proveidor(nom, correu_electronic, direccio, telefon, db)
    return result

@app.put("/update_proveidor/", response_model=dict)
async def update_telefon_proveidor(nom: str, telefon: str, db: Session = Depends(get_db)):
    result = proveidor.update_proveidor_telefon(nom, telefon, db)
    return result

@app.delete("/proveidor/delete/", response_model=dict)
async def del_proveidor(nom: str, db: Session = Depends(get_db)):
    result = proveidor.delete_proveidor(nom, db)
    return result

