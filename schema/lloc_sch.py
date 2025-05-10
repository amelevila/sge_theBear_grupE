def lloc_schema(lloc) -> dict:
    response = {"lloc": lloc}
    return response

def llocs_schema(llocs) -> list[dict]:
    response = [lloc_schema(lloc) for lloc in llocs]
    return response