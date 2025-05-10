from sqlmodel import Session, select
from models.Empleat import Empleat
from schema.empleat_sch import empleats_schema

def llegir_empleats(db: Session):
    statement = select(Empleat)
    empleats = db.exec(statement).all()
    return empleats_schema(empleats)

def afegir_empleat(nom: str, carrec: str, curriculum: str, habilitats: str, telefon: int, email: str, db: Session):
    db_empleat = Empleat(
        nom=nom,
        carrec=carrec,
        curriculum=curriculum,
        habilitats=habilitats,
        telefon=telefon,
        email=email
    )
    db.add(db_empleat)
    db.commit()
    db.refresh(db_empleat)
    return {"msg": "Empleat creat exitosament"}

def update_empleat_email(nom: str, email: str, db: Session):
    statement = select(Empleat).where(Empleat.nom == nom)
    result = db.exec(statement).one()
    result.email = email
    db.commit()
    return {"msg": "Email actualitzat exitosament"}

def delete_empleat(nom: str, db: Session):
    statement = select(Empleat).where(Empleat.nom == nom)
    result = db.exec(statement).one()
    db.delete(result)
    db.commit()
    return {"msg": "Empleat eliminat exitosament"}