def encarrec_schema(encarrec) -> dict:
    response = {"encarrec": encarrec}
    return response

def encarrecs_schema(encarrecs) -> list[dict]:
    response = [encarrec_schema(encarrec) for encarrec in encarrecs]
    return response
