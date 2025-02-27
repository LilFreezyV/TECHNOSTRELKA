import psycopg2
import config
import pandas as pd

config.read_config()

df = pd.read_csv('final_dataset.csv')

conn = psycopg2.connect(
        dbname=config.get_param_value('dbname'),
        user=config.get_param_value('dbuser'),
        password=config.get_param_value('dbpwd'),
        host=config.get_param_value('dbhost'),
        port=int(config.get_param_value('dbport')))
cursor = conn.cursor()

data = []

for _, row in df.iterrows():
    data.append((row['title'], row['text'], row['text_lemm'], row['genre']))
    
query = f'''
insert into films (title, description, text_lemm, genre)
values (%s, %s, %s, %s)
'''
cursor.executemany(query, data)
conn.commit()
conn.close()