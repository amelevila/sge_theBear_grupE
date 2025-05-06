from datetime import date
from sqlmodel import Session, select
from schema.punts_de_venda_sch import punts_de_venda_schema
from models.Punts_de_venda import Punt_de_venda


def llegir_punts_de_venda(db:Session):
    sql_read = select(Punt_de_venda)
    client = db.exec(sql_read).all()
    return punts_de_venda_schema(client)

def afegir_punts_de_venda(lloc: str, calendari: date, venta: str, db: Session):
    db_punt_de_venda = Punt_de_venda(lloc=lloc, calendari=calendari, venta=venta)
    db.add(db_punt_de_venda)
    db.commit()
    db.refresh(db_punt_de_venda)
    return {"msg":"Punt de venda afegit correctament."}

def update_punt_de_venda_venda(lloc: str, venda:str, db: Session):
    statement = select(Punt_de_venda).where(Punt_de_venda.lloc == lloc)
    results = db.exec(statement)
    punt_de_venda = results.one()
    punt_de_venda.venda = venda
    db.add(punt_de_venda)
    db.commit()
    return {"msg":"Venda actualitzada amb èxit"}

def update_punt_de_venda_lloc(lloc: str, venda:str, db: Session):
    statement = select(Punt_de_venda).where(Punt_de_venda.venda == venda)
    results = db.exec(statement)
    punt_de_venda = results.one()
    punt_de_venda.lloc = lloc
    db.add(punt_de_venda)
    db.commit()
    return {"msg":"Lloc actualitzat amb èxit"}

def delete_punt_de_venda(lloc: str, db:Session):
    statement = select(Punt_de_venda).where(Punt_de_venda.lloc == lloc)
    results = db.exec(statement)
    punt_de_venda = results.one()
    db.delete(punt_de_venda)
    db.commit()
    return {"msg":"Punt de venda esborrat amb èxit."}
