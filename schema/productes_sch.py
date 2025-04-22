def producte_schema(producte) -> dict:
    response = {"producte":producte}
    return response

def productes_schema(productes)-> list[dict]:
    response = [productes_schema(producte) for producte in productes]
    return response