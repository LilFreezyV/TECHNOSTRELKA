import psycopg2
import config
import pandas as pd

config.read_config()

conn = psycopg2.connect(
        dbname=config.get_param_value('dbname'),
        user=config.get_param_value('dbuser'),
        password=config.get_param_value('dbpwd'),
        host=config.get_param_value('dbhost'),
        port=int(config.get_param_value('dbport')))
cursor = conn.cursor()

df = pd.read_csv('final_dataset_full.csv')

data = []

for _, row in df.iterrows():
    data.append((row['title'], row['text'], row['text_lemm'], row['genre'], row['imglink']))
    
query = f'''
insert into films_full (title, description, text_lemm, genre, imglink)
values (%s, %s, %s, %s, %s)
'''
cursor.executemany(query, data)
conn.commit()

df = pd.read_csv('final_dataset_short.csv')

data = []

for _, row in df.iterrows():
    data.append((row['title'], row['description'], row['genre'], row['imglink']))
    
query = f'''
insert into films_full (title, description, text_lemm, genre, imglink)
values (%s, %s, %s, %s, %s)
'''
cursor.executemany(query, data)
conn.commit()

conn.close()