def punt_de_venda_schema(punt_de_venda) -> dict:
    response = {"Punt de venda": punt_de_venda}
    return response

def punts_de_venda_schema(punts_de_venda) -> list[dict]:
    response = [punts_de_venda(punt_de_venda) for punt_de_venda in punts_de_venda]
    return response