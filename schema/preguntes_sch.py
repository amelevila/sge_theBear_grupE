def pregunta_schema(pregunta) -> dict:
    response = {"pregunta":pregunta}
    return response

def preguntes_schema(preguntes)-> list[dict]:
    response = [pregunta_schema(pregunta) for pregunta in preguntes]
    return response