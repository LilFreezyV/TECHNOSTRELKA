import psycopg2

conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='postgres',
        host='46.29.160.85',
        port=5432)
cursor = conn.cursor()

query = """
create table users (
    id serial primary key,
    username text,
    surname text,
    name text,
    number text,
    email text,
    password text,
    created_date timestamp
)
"""

cursor.execute(query)
conn.commit()