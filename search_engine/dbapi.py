import psycopg2

def get_user_id(username: str, password: str) -> int:
    def my_query(cursor):
        query = f"""
        select
            id
        from
            test_table
        where
            name = '{username}'
            and pwd = '{password}'
        """
        cursor.execute(query)
        return cursor.fetchone()
    res = execute(my_query)
    if res == None:
        return -1
    return res[0]

def get_users(username: str) -> list:
    def my_query(cursor):
        query = f"""
        select
            id
        from
            test_table
        """

def execute(dbfun):
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='postgres',
        host='46.29.160.85',
        port=5432)
    cursor = conn.cursor()
    res = dbfun(cursor)
    conn.commit()
    conn.close()
    return res
