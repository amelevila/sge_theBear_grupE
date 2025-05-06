def comunicacio_schema(comunicacio) -> dict:
    response = {"comunicacio":comunicacio}
    return response

def comunicacions_schema(comunicacions)-> list[dict]:
    response = [comunicacio_schema(comunicacio) for comunicacio in comunicacions]
    return response