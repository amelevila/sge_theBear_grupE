def torn_schema(torn) -> dict:
    response = {"torn": torn}
    return response

def torns_schema(torns) -> list[dict]:
    response = [torn_schema(torn) for torn in torns]
    return response
