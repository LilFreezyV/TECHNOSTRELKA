import psycopg2
import search_engine.config as config

config.read_config()

conn = psycopg2.connect(
        dbname=config.get_param_value('dbname'),
        user=config.get_param_value('dbuser'),
        password=config.get_param_value('dbpwd'),
        host=config.get_param_value('dbhost'),
        port=int(config.get_param_value('dbport')))
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