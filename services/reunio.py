from schema.reunions_sch import reunions_schema
from sqlmodel import Session, select
from models.Reunio import Reunio
from datetime import date, time

def llegir_reunions(db:Session):
    sql_read = select(Reunio)
    reunio = db.exec(sql_read).all()
    return reunions_schema(reunio)

def afegir_reunio(assumpte: str, organitzador: str, privacitat: str, data_inici: date, duracio: int, ubicacio: str, url: str, descripcio: str, db:Session):
    db_reunio = Reunio(assumpte=assumpte, organitzador=organitzador, privacitat=privacitat, data_inici=data_inici, duracio=duracio, ubicacio=ubicacio, url=url, descripcio=descripcio)
    db.add(db_reunio)
    db.commit()
    db.refresh(db_reunio)
    return {"msg":"Reunio creada exitosament"}

def update_reunio_duracio(assumpte: str, duracio: int, db:Session):
    statement = select(Reunio).where(Reunio.assumpte == assumpte)
    results = db.exec(statement)
    reunio = results.one()
    reunio.duracio = duracio
    db.add(reunio)
    db.commit()
    return {"msg":"Duració actualitzada exitosament"}

def delete_reunio(assumpte: str, db:Session):
    statement = select(Reunio).where(Reunio.assumpte == assumpte)
    results = db.exec(statement)
    reunio = results.one()
    db.delete(reunio)
    db.commit()
    return {"msg":"Reunio eliminat exitosament"}