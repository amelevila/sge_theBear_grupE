from schema.clients_sch import clients_schema
from sqlmodel import Session, select
from models.Client import Client

def llegir_clients(db:Session):
    sql_read = select(Client)
    client = db.exec(sql_read).all()
    return clients_schema(client)

def afegir_client(nom: str, email: str, residencia: str, db:Session):
    db_client = Client(nom=nom, email=email, residencia=residencia)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return {"msg":"Client creat exitosament"}

def update_client_email(nom: str, email: str, db:Session):
    statement = select(Client).where(Client.nom == nom)
    results = db.exec(statement)
    client = results.one()
    client.email = email
    db.add(client)
    db.commit()
    return {"msg":"Email actualitzat exitosament"}

def delete_client(nom: str, db:Session):
    statement = select(Client).where(Client.nom == nom)
    results = db.exec(statement)
    client = results.one()
    db.delete(client)
    db.commit()
    return {"msg":"Client eliminat exitosament"}