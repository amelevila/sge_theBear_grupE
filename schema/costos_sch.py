def cost_schema(cost) -> dict:
    response = {"cost":cost}
    return response

def costos_schema(costos)-> list[dict]:
    response = [cost_schema(cost) for cost in costos]
    return response