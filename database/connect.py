import psycopg2

def connection_db():
    conn = psycopg2.connect(
        databases="the_bear",
        password="admin",
        user="admin",
        host="localhost",
        port="5432"
    )

    return conn