from schema.productes_sch import productes_schema
from sqlmodel import Session, select
from models.Producte import Producte

def llegir_productes(db:Session):
    sql_read = select(Producte)
    producte = db.exec(sql_read).all()
    return productes_schema(producte)

def  afegir_producte(nom: str, preu: int, valoracio: int, db:Session):
    db_producte = Producte(nom=nom, preu=preu, valoracio=valoracio)
    db.add(db_producte)
    db.commit()
    db.refresh(db_producte)
    return {"Producte creat exitosament"}

def update_producte_preu(nom: str, preu: int, db:Session):
    statement = select(Producte).where(Producte.nom == nom)
    results = db.exec(statement)
    producte = results.one()
    producte.preu = preu
    db.add(producte)
    db.commit()
    return {"Preu actualitzat exitosament"}

def delete_producte(nom: str, db:Session):
    statement = select(Producte).where(Producte.nom == nom)
    results = db.exec(statement)
    producte = results.one()
    db.delete(producte)
    db.commit()
    return {"Producte eliminat exitosament"}