from schema.clients_sch import clients_schema
from sqlmodel import Session, select
from models.Client import Client

def llegir_clients(db:Session):
    sql_read = select(Client)
    client = db.exec(sql_read).all()
    return clients_schema(client)

def  afegir_client(nom: str, email: str, residencia: str, db:Session):
    db_client = Client(nom=nom, email=email, residencia=residencia)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return {"Client creat exitosament"}

def update_client_comercial(nom: str, comercial: str, db:Session):
    statement = select(Client).where(Client.nom == nom)
    results = db.exec(statement)
    client = results.one()
    client.nom = nom
    db.add(client)
    db.commit()
    return {"Comercial actualitzat exitosament"}

def delete_client(numero: int, db:Session):
    statement = select(Client).where(Client.numero == numero)
    results = db.exec(statement)
    client = results.one()
    db.delete(client)
    db.commit()
    return {"Client eliminat exitosament"}