def producte_compra_schema(producte_compra) -> dict:
    response = {"producte_compra": producte_compra}
    return response

def productes_compra_schema(productes_compra) -> list[dict]:
    response = [producte_compra_schema(producte_compra) for producte_compra in productes_compra]
    return response
