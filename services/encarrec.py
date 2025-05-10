from schema.encarrecs_sch import encarrecs_schema
from sqlmodel import Session, select
from models.Encarrec import Encarrec
from datetime import date

def llegir_encarrecs(db: Session):
    sql_read = select(Encarrec)
    encarrec = db.exec(sql_read).all()
    return encarrecs_schema(encarrec)

def afegir_encarrec(nom: str, proveïdor: str, data_limit: date, data_recollida: date, db: Session):
    db_encarrec = Encarrec(nom=nom, proveïdor=proveïdor, data_limit=data_limit, data_recollida=data_recollida)
    db.add(db_encarrec)
    db.commit()
    db.refresh(db_encarrec)
    return {"msg": "Encarrec creat exitosament"}

def update_encarrec_data(nom: str, data_recollida: date, db: Session):
    statement = select(Encarrec).where(Encarrec.nom == nom)
    results = db.exec(statement)
    encarrec = results.one()
    encarrec.data_recollida = data_recollida
    db.add(encarrec)
    db.commit()
    return {"msg": "Data de recollida actualitzada exitosament"}

def delete_encarrec(nom: str, db: Session):
    statement = select(Encarrec).where(Encarrec.nom == nom)
    results = db.exec(statement)
    encarrec = results.one()
    db.delete(encarrec)
    db.commit()
    return {"msg": "Encarrec eliminat exitosament"}
