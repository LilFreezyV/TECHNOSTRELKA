import psycopg2
import config
import pandas as pd

def concat_tuples(tuples):
    res = ()
    for t in tuples:
        res += t
    return res

config.read_config()

conn = psycopg2.connect(
        dbname=config.get_param_value('dbname'),
        user=config.get_param_value('dbuser'),
        password=config.get_param_value('dbpwd'),
        host=config.get_param_value('dbhost'),
        port=int(config.get_param_value('dbport')))
cursor = conn.cursor()

# df = pd.read_csv('final_dataset_full.csv')
# print('full_dataset прочитан')

# data = []
# print('извлечение')
# for _, row in df.iterrows():
#     data.append((row['title'], row['text'], row['text_lemm'], row['genre'], ''))

# print('извлечено')

# query = f'''
# insert into films_full (title, description, text_lemm, genre, imglink)
# values {"(%s, %s, %s, %s, %s)," * 100}
# '''
# print('запись в бд')
# for i in range(0, len(data), 100):
#     cursor.execute(query[:len(query)-2], concat_tuples(data[i:i+100]))
#     conn.commit()
#     print('запрос успешен')
# print('записано')


df = pd.read_csv('final_dataset_short.csv')
print('short_dataset прочитан')
data = []
print('извлечение')
for _, row in df.iterrows():
    data.append(('None' if row['title'] == None else row['title'], 'None' if row['text'] == None else row['text'], 'None' if row['title'] == None else row['title'], ''))
print(len(data))
print('извлечено')
query = f'''
insert into films_full (title, description, genre, imglink)
values {"(%s, %s, %s, %s), " * 100}
'''
print('запись в бд')
for i in range(0, len(data), 100):
    cursor.execute(query[:len(query)-3], concat_tuples(data[i:i+100]))
    conn.commit()
    print('запрос успешен')
print('записано')


conn.close()