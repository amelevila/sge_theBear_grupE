from schema.torns_sch import torns_schema
from sqlmodel import Session, select
from models.Torn import Torn
from datetime import date

def llegir_torns(db: Session):
    sql_read = select(Torn)
    torn = db.exec(sql_read).all()
    return torns_schema(torn)

def afegir_torn(nom: str, recurs: str, data: date, minuts: int, db: Session):
    db_torn = Torn(nom=nom, recurs=recurs, data=data, minuts=minuts)
    db.add(db_torn)
    db.commit()
    db.refresh(db_torn)
    return {"msg": "Torn creat exitosament"}

def update_torn_minuts(nom: str, minuts: int, db: Session):
    statement = select(Torn).where(Torn.nom == nom)
    results = db.exec(statement)
    torn = results.one()
    torn.minuts = minuts
    db.add(torn)
    db.commit()
    return {"msg": "Minuts actualitzats exitosament"}

def delete_torn(nom: str, db: Session):
    statement = select(Torn).where(Torn.nom == nom)
    results = db.exec(statement)
    torn = results.one()
    db.delete(torn)
    db.commit()
    return {"msg": "Torn eliminat exitosament"}
