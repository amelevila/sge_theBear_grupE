from schema.costos_sch import costos_schema
from sqlmodel import Session, select
from models.Cost import Cost
from datetime import date

def llegir_costos(db:Session):
    sql_read = select(Cost)
    costos = db.exec(sql_read).all()
    return costos_schema(costos)

def afegir_cost(numero: int, nom_client: str, comercial: str, venciment: date, nom_producte: str, db:Session):
    db_cost = Cost(numero=numero, nom_client=nom_client, comercial=comercial, venciment=venciment, nom_producte=nom_producte)
    db.add(db_cost)
    db.commit()
    db.refresh(db_cost)
    return {"msg":"Cost creat exitosament"}

def update_cost_comercial(numero: int, comercial: str, db:Session):
    statement = select(Cost).where(Cost.numero == numero)
    results = db.exec(statement)
    cost = results.one()
    cost.comercial = comercial
    db.add(cost)
    db.commit()
    return {"msg":"Comercial actualitzat exitosament"}

def delete_cost(numero: int, db:Session):
    statement = select(Cost).where(Cost.numero == numero)
    results = db.exec(statement)
    cost = results.one()
    db.delete(cost)
    db.commit()
    return {"msg":"Cost eliminat exitosament"}