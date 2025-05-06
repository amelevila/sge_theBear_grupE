def configuracio_schema(configuracio) -> dict:
    response = {"configuracio":configuracio}
    return response

def configuracions_schema(configuracions)-> list[dict]:
    response = [configuracio_schema(configuracio) for configuracio in configuracions]
    return response