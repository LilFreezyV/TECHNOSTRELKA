import psycopg2
import config

config.read_config()

conn = psycopg2.connect(
        dbname=config.get_param_value('dbname'),
        user=config.get_param_value('dbuser'),
        password=config.get_param_value('dbpwd'),
        host=config.get_param_value('dbhost'),
        port=int(config.get_param_value('dbport')))
cursor = conn.cursor()

query = """
create table if not exists users (
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


# Для рекомендательной системы
query = """
create table if not exists genres (
	id serial primary key,
	name text not null
)
"""
cursor.execute(query)
conn.commit()


query = """
create table if not exists user_genres (
	id serial primary key,
	uid integer references users (id) not null,
	gid integer references genres (id) not null,
	queries_count integer not null
)
"""
cursor.execute(query)
conn.commit()


conn.close()
