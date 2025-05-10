def vista_schema(vista) -> dict:
    response = {"vista": vista}
    return response

def vistes_schema(vistes) -> list[dict]:
    response = [vista_schema(vista) for vista in vistes]
    return response
