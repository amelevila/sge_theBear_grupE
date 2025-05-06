from schema.lloc_sch import lloc_schema
from sqlmodel import Session, select
from models.Lloc import Lloc

def llegir_lloc(db:Session):
    sql_read = select(Lloc)
    lloc = db.exec(sql_read).all()
    return lloc_schema(lloc)

def afegir_lloc(id:int, num_taula: int, lliure:bool, db: Session):
    db_lloc = Lloc(id=id, num_taula = num_taula, lliure = lliure)
    db.add(db_lloc)
    db.commit()
    db.refresh(db_lloc)
    return {"msg":"Lloc creat correctament."}

def update_lloc_lliure(num_taula:int, lliure:bool, db:Session):
    statement = select(Lloc).where(Lloc.num_taula == num_taula)
    results = db.exec(statement)
    lloc = results.one()
    lloc.lliure = lliure
    db.add(lloc)
    db.commit()
    return {"msg":"Disponibilitat de la taula actualitzada."}

def delete_lloc(num_taula: int, db: Session):
    statement = select(Lloc).where(Lloc.num_taula == num_taula)
    results = db.exec(statement)
    client = results.one()
    db.delete(client)
    db.commit()
    return {"msg":"Lloc esborrat amb exit."}