def event_schema(event) -> dict:
    response = {"event":event}
    return response

def events_schema(events)-> list[dict]:
    response = [event_schema(event) for event in events]
    return response