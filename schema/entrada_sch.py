def entrada_schema(entrada) -> dict:
    response = {"entrada":entrada}
    return response

def entrades_schema(entrades)-> list[dict]:
    response = [entrada_schema(entrada) for entrada in entrades]
    return response