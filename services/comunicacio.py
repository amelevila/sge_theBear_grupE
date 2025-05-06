from sqlmodel import Session, select
from models.comunicacio import Comunicacio
from schema.comunicacio_sch import comunicacions_schema

def llegir_comunicacions(db: Session):
    statement = select(Comunicacio)
    comunicacions = db.exec(statement).all()
    return comunicacions_schema(comunicacions)

def afegir_comunicacio(plantilla: str, unitat: int, activacio: str, db: Session):
    db_comunicacio = Comunicacio(
        plantilla=plantilla,
        unitat=unitat,
        activacio=activacio
    )
    db.add(db_comunicacio)
    db.commit()
    db.refresh(db_comunicacio)
    return {"msg": "Comunicació creada exitosament"}

def update_comunicacio_activacio(plantilla: str, nova_activacio: str, db: Session):
    statement = select(Comunicacio).where(Comunicacio.plantilla == plantilla)
    comunicacio = db.exec(statement).one()
    comunicacio.activacio = nova_activacio
    db.commit()
    return {"msg": "Activació actualitzada correctament"}

def delete_comunicacio(plantilla: str, db: Session):
    statement = select(Comunicacio).where(Comunicacio.plantilla == plantilla)
    comunicacio = db.exec(statement).one()
    db.delete(comunicacio)
    db.commit()
    return {"msg": "Comunicació eliminada correctament"}