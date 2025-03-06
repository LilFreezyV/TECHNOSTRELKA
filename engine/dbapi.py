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

def get_current_users(username: str) -> list:
    def my_query(cursor):
        query = f"""
        select
            username
        from
            users
        where
            username = '{username}'
        """
        cursor.execute(query)
        return cursor.fetchall()
    res = execute(my_query)
    return res

def get_user_by_id(uid: int):
    def my_query(cursor):
        query=f"""
        select 
            username,
            surname,
            name,
            number,
            email
        from users
        where id = {uid}
        """
        cursor.execute(query)
        return cursor.fetchone()
    res = execute(my_query)
    return res

def get_full_films() -> list:
    def my_query(cursor):
        query = f"""
        select
            title,
            description,
            text_lemm,
            genre,
            imglink
        from
            films_full
        """
        cursor.execute(query)
        return cursor.fetchall()
    res = execute(my_query)
    return res

def get_short_films() -> list:
    def my_query(cursor):
        query = f"""
        select
            title,
            description,
            genre,
            imglink
        from
            films_short
        """
        cursor.execute(query)
        return cursor.fetchall()
    res = execute(my_query)
    return res

def get_recfilm(uid: int) -> str:
    def my_query(cursor):
        query = f"""
        select
            urec
        from
            user_recs
        where
            uid = {uid}
        """
        cursor.execute(query)
        return cursor.fetchone()
    res = execute(my_query)
    return res[0]

def set_recfilm(uid: int) -> None:
    def my_query(cursor):
        query = f"""
        insert into user_recs (uid, urec)
        values (%s, %s)
        """
        cursor.execute(query, (uid, 'Interstellar Wars (2016)'))
    execute(my_query)


def update_user_recs(uid: int, rectitle: str) -> None:
    def my_query(cursor):
        query = f"""
        update user_recs
        set urec = %s
        where uid = %s
        """
        cursor.execute(query, (rectitle, uid))
    execute(my_query)


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
    conn = psycopg2.connect(
        dbname=config.get_param_value('dbname'),
        user=config.get_param_value('dbuser'),
        password=config.get_param_value('dbpwd'),
        host=config.get_param_value('dbhost'),
        port=int(config.get_param_value('dbport'))
    )

    cursor = conn.cursor()
    res = dbfun(cursor)
    conn.commit()
    conn.close()
    return res
