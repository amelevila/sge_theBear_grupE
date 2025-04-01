import psycopg2

def connection_db():
    conn = psycopg2.connect(
            database="the_bear",
            password="pass",
            user="user",
            host="localhost",
            port="5432"
        )

    return conn

conexio = connection_db()
print(conexio)
conexio.close()
print(conexio)
