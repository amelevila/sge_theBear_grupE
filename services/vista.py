from schema.vistes_sch import vistes_schema
from sqlmodel import Session, select
from models.Vista import Vista
from datetime import date

def llegir_vistes(db: Session):
    sql_read = select(Vista)
    vista = db.exec(sql_read).all()
    return vistes_schema(vista)

def afegir_vista(nom: str, data: date, db: Session):
    db_vista = Vista(nom=nom, data=data)
    db.add(db_vista)
    db.commit()
    db.refresh(db_vista)
    return {"msg": "Vista creada exitosament"}

def update_vista_data(nom: str, data: date, db: Session):
    statement = select(Vista).where(Vista.nom == nom)
    results = db.exec(statement)
    vista = results.one()
    vista.data = data
    db.add(vista)
    db.commit()
    return {"msg": "Data actualitzada exitosament"}

def delete_vista(nom: str, db: Session):
    statement = select(Vista).where(Vista.nom == nom)
    results = db.exec(statement)
    vista = results.one()
    db.delete(vista)
    db.commit()
    return {"msg": "Vista eliminada exitosament"}
