from schema.proveidors_sch import proveidors_schema
from sqlmodel import Session, select
from models.Proveidor import Proveidor

def llegir_proveidors(db: Session):
    sql_read = select(Proveidor)
    proveidor = db.exec(sql_read).all()
    return proveidors_schema(proveidor)

def afegir_proveidor(nom: str, correu_electronic: str, direccio: str, telefon: str, db: Session):
    db_proveidor = Proveidor(nom=nom, correu_electronic=correu_electronic, direccio=direccio, telefon=telefon)
    db.add(db_proveidor)
    db.commit()
    db.refresh(db_proveidor)
    return {"msg": "Proveïdor creat exitosament"}

def update_proveidor_telefon(nom: str, telefon: str, db: Session):
    statement = select(Proveidor).where(Proveidor.nom == nom)
    results = db.exec(statement)
    proveidor = results.one()
    proveidor.telefon = telefon
    db.add(proveidor)
    db.commit()
    return {"msg": "Telèfon actualitzat exitosament"}

def delete_proveidor(nom: str, db: Session):
    statement = select(Proveidor).where(Proveidor.nom == nom)
    results = db.exec(statement)
    proveidor = results.one()
    db.delete(proveidor)
    db.commit()
    return {"msg": "Proveïdor eliminat exitosament"}
