from sqlmodel import Session, select
from models.Entrada import Entrada
from schema.entrada_sch import entrades_schema
from datetime import date

def llegir_entrades(db: Session):
    statement = select(Entrada)
    result = db.exec(statement).all()
    return entrades_schema(result)

def afegir_entrada(producte: str, nom: str, preu: float, data_ventes: date, maxim_persones: int, db: Session):
    db_entrada = Entrada(
        producte=producte,
        nom=nom,
        preu=preu,
        data_ventes=data_ventes,
        maxim_persones=maxim_persones
    )
    db.add(db_entrada)
    db.commit()
    db.refresh(db_entrada)
    return {"msg": "Entrada creada exitosament"}

def update_entrada_preu(producte: str, nou_preu: float, db: Session):
    statement = select(Entrada).where(Entrada.producte == producte)
    entrada = db.exec(statement).one()
    entrada.preu = nou_preu
    db.commit()
    return {"msg": "Preu actualitzat correctament"}

def delete_entrada(producte: str, db: Session):
    statement = select(Entrada).where(Entrada.producte == producte)
    entrada = db.exec(statement).one()
    db.delete(entrada)
    db.commit()
    return {"msg": "Entrada eliminada correctament"}