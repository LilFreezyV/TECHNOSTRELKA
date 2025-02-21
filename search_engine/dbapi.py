import psycopg2
import config

config.read_config()

def get_user_id(username: str, password: str) -> int:
    def my_query(cursor):
        query = f"""
        select
            id
        from
            users
        where
            username = '{username}'
            and password = '{password}'
        """
        cursor.execute(query)
        return cursor.fetchone()
    res = execute(my_query)
    if res == None:
        return -1
    return res[0]

def get_users() -> list:
    def my_query(cursor):
        query = f"""
        select
            username
        from
            users
        """
        cursor.execute(query)
        return cursor.fetchall()
    res = execute(my_query)
    return res

def add_user(username: str, surname: str, name: str, number: str, email: str, password: str) -> int:
    def my_query(cursor):
        query = f"""
        insert into
            users (username, surname, name, number, email, password)
        values
            ('{username}', '{surname}', '{name}', '{number}', '{email}', '{password}')
        returning
            id
        """
        cursor.execute(query)
        return cursor.fetchone()
    res = execute(my_query)
    return res[0]

def execute(dbfun):
    print(f'''dbname={config.get_param_value('dbname')},
        user={config.get_param_value('dbuser')},
        password={config.get_param_value('dbpwd')},
        host={config.get_param_value('dbhost')},
        port={config.get_param_value('dbport')}''')
    try:
        conn = psycopg2.connect(
            dbname=config.get_param_value('dbname'),
            user=config.get_param_value('dbuser'),
            password=config.get_param_value('dbpwd'),
            host=config.get_param_value('dbhost'),
            port=int(config.get_param_value('dbport')))
    except Exception as e:
        print(e)
    cursor = conn.cursor()
    res = dbfun(cursor)
    conn.commit()
    conn.close()
    return res
