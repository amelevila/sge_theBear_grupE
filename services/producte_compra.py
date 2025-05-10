from schema.productes_compra_sch import productes_compra_schema
from sqlmodel import Session, select
from models.Producte_compra import Producte_compra

def llegir_productes_compra(db: Session):
    sql_read = select(Producte_compra)
    producte_compra = db.exec(sql_read).all()
    return productes_compra_schema(producte_compra)

def afegir_producte_compra(nom: str, tipus: str, preu: int, categoria: str, db: Session):
    db_producte_compra = Producte_compra(nom=nom, tipus=tipus, preu=preu, categoria=categoria)
    db.add(db_producte_compra)
    db.commit()
    db.refresh(db_producte_compra)
    return {"msg": "Producte de compra creat exitosament"}

def update_producte_compra_preu(nom: str, preu: int, db: Session):
    statement = select(Producte_compra).where(Producte_compra.nom == nom)
    results = db.exec(statement)
    producte_compra = results.one()
    producte_compra.preu = preu
    db.add(producte_compra)
    db.commit()
    return {"msg": "Preu actualitzat exitosament"}

def delete_producte_compra(nom: str, db: Session):
    statement = select(Producte_compra).where(Producte_compra.nom == nom)
    results = db.exec(statement)
    producte_compra = results.one()
    db.delete(producte_compra)
    db.commit()
    return {"msg": "Producte de compra eliminat exitosament"}
