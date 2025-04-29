def nota_schema(nota) -> dict:
    response = {"nota":nota}
    return response

def notes_schema(notes)-> list[dict]:
    response = [nota_schema(nota) for nota in notes]
    return response