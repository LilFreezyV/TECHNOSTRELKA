from typing import Tuple
import modelapi
import dbapi
import recsapi
# import movieposters as mp
from googletrans import Translator
from typing import Tuple

# TEST_CONTENT = ['КОНТЕНТ ЗАПР', 'КОНТЕНТ ЗАПР', 'КОНТЕНТ ЗАПР', 'КОНТЕНТ ЗАПР']
# TEST_RECS = [
#     {'title': 'avatar (2023)', 'text': 'aaa aa aaaaa bbb bbbb bbbb', 'genre': 'drama', 'link': mp.get_poster('avatar')},
#     {'title': 'avengers (2024)', 'text': 'we3e23e23e333', 'genre': 'action', 'link': mp.get_poster('avengers')},
#     {'title': 'forest gamp (2023)', 'text': 'aaa aa aaaaa bbb bbbb bbbb', 'genre': 'drama',
#      'link': mp.get_poster('forest gamp')},
#     {'title': 'star wars (2024)', 'text': 'we3e23e23e333', 'genre': 'action',
#      'link': mp.get_poster('star wars')},
#     {'title': 'avatar (2023)', 'text': 'aaa aa aaaaa bbb bbbb bbbb', 'genre': 'drama', 'link': mp.get_poster('avatar')},
#     {'title': 'avengers (2024)', 'text': 'we3e23e23e333', 'genre': 'action', 'link': mp.get_poster('avengers')},
#     {'title': 'avatar (2023)', 'text': 'aaa aa aaaaa bbb bbbb bbbb', 'genre': 'drama', 'link': mp.get_poster('avatar')},
#     {'title': 'avengers (2024)', 'text': 'we3e23e23e333', 'genre': 'action', 'link': mp.get_poster('avengers')},
# ]


translator = Translator()


def login(username: str, password: str) -> Tuple[int, str]:
    uid = dbapi.get_user_id(username, password)
    status = "OK"
    if uid == -1:
        status = "USER NOT FOUND"
    return uid, status


def register(username: str, surname: str, name: str, number: str, email: str, password: str) -> Tuple[int, str]:
    users = dbapi.get_current_users(username)
    if len(users) > 0:
        return -1, "LOGIN ALREADY TAKEN"
    uid = dbapi.add_user(username, surname, name, number, email, password)
    dbapi.set_recfilm(uid)
    return uid, "OK"

def update_userinfo(uid: int, rectitle: str) -> None:
    dbapi.update_user_recs(uid, rectitle)

def find_by_query(query: str, uid: int) -> list[dict]:
    translation = translator.translate(text=query, dest='en')
    res = modelapi.process_query(translation.text)
    update_userinfo(uid, res[0]['title'])
    return res

def get_recfilm(uid: int):
    return dbapi.get_recfilm(uid)

def get_recs(uid: int) -> Tuple[list[dict], str]:
    try:
        rectitle = get_recfilm(uid)
        return recsapi.give_recomendations(rectitle), "ok"
    except:
        return [], "error"
