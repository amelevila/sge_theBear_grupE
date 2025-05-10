def punts_de_venda_schema(pdv) -> dict:
    response = {"punts_de_venda": pdv}
    return response

def punts_de_venda_list_schema(pdv_list) -> list[dict]:
    response = [punts_de_venda_schema(pdv) for pdv in pdv_list]
    return response
