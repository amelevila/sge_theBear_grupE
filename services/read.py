from schema import read_sch

def registre():
    users = {
        "user1":{
            "id":1,
            "name":"Izan",
            "surname":"Duarte",
            "age":49
        },
        "user2": {
            "id":1,
            "name":"Josep Oriol",
            "surname":"Roca",
            "age":23
        },
        "user3": {
            "id":3,
            "name":"Juan Manuel",
            "surname":"Sanchez",
            "age":40
        }
    }
    return read_sch.schemas(users)