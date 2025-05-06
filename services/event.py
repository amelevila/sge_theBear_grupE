from sqlmodel import Session, select
from models.event import Event
from schema.event_sch import events_schema
from datetime import date

def llegir_events(db: Session):
    statement = select(Event)
    result = db.exec(statement).all()
    return events_schema(result)

def afegir_event(nou_event: str, reservats: str, anunciats: str, informes: str, data: date, db: Session):
    db_event = Event(
        nou_event=nou_event,
        reservats=reservats,
        anunciats=anunciats,
        informes=informes,
        data=data
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return {"msg": "Event creat exitosament"}

def update_event_data(event_id: int, nova_data: date, db: Session):
    statement = select(Event).where(Event.id == event_id)
    event = db.exec(statement).one()
    event.data = nova_data
    db.commit()
    return {"msg": "Data de l'event actualitzada"}

def delete_event(event_id: int, db: Session):
    statement = select(Event).where(Event.id == event_id)
    event = db.exec(statement).one()
    db.delete(event)
    db.commit()
    return {"msg": "Event eliminat correctament"}