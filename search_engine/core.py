from typing import Tuple
import modelapi
import dbapi
import movieposters as mp

TEST_CONTENT = ['КОНТЕНТ ЗАПР', 'КОНТЕНТ ЗАПР', 'КОНТЕНТ ЗАПР', 'КОНТЕНТ ЗАПР']
TEST_RECS = [
    {'title': 'avatar (2023)', 'text': 'aaa aa aaaaa bbb bbbb bbbb', 'genre': 'drama', 'link': mp.get_poster('avatar')},
    {'title': 'avengers (2024)', 'text': 'we3e23e23e333', 'genre': 'action', 'link': mp.get_poster('avengers')},
    {'title': 'forest gamp (2023)', 'text': 'aaa aa aaaaa bbb bbbb bbbb', 'genre': 'drama',
     'link': mp.get_poster('forest gamp')},
    {'title': 'star wars (2024)', 'text': 'we3e23e23e333', 'genre': 'action',
     'link': mp.get_poster('star wars')},
    {'title': 'avatar (2023)', 'text': 'aaa aa aaaaa bbb bbbb bbbb', 'genre': 'drama', 'link': mp.get_poster('avatar')},
    {'title': 'avengers (2024)', 'text': 'we3e23e23e333', 'genre': 'action', 'link': mp.get_poster('avengers')},
    {'title': 'avatar (2023)', 'text': 'aaa aa aaaaa bbb bbbb bbbb', 'genre': 'drama', 'link': mp.get_poster('avatar')},
    {'title': 'avengers (2024)', 'text': 'we3e23e23e333', 'genre': 'action', 'link': mp.get_poster('avengers')},
]


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
    return uid, "OK"

def find_by_query(query: str) -> list[dict]:
    return modelapi.process_query(query)

# def get_tags(query: str) -> list[object]:
#     return modelapi.process_query(query)

# def update_userinfo(tags: list[object], uid: int = 0) -> None:
#     pass

# def find_by_tags(tags: list[object]) -> list[object]:
    # return TEST_CONTENT # Временно

def get_recs(uid: int = 0) -> list[object]:
    return TEST_RECS  # Временно


def process_query(query: str) -> list[object]:
    # tags = get_tags(query)
    # result = find_by_tags(tags)
    # update_userinfo(tags)
    # return result
    pass


