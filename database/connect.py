import psycopg2

def connection():
    conn = psycopg2.connect(
        database="all_penjat",
        password="pass",
        user="user",
        host="localhost",
        port="5433"
    )

    return conn