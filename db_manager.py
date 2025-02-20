import sqlite3

all_usernames = []


def get_users():
    con = sqlite3.connect('db/users.db')
    cur = con.cursor()
    data = list(cur.execute("""SELECT username FROM users"""))
    for elem in data:
        all_usernames.append(elem[0])
    return all_usernames


def check_user(username, password):
    con = sqlite3.connect('db/users.db')
    cur = con.cursor()
    input_user = (username,)
    _id = list(cur.execute(f"""SELECT id FROM users WHERE username LIKE ?""", input_user))[0][0]
    real_password = list(cur.execute(f"""SELECT password FROM users WHERE id = {_id}"""))[0][0]
    if password == real_password:
        return True
    return False
