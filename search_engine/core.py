from typing import Tuple
import dbapi

TEST_CONTENT = ['КОНТЕНТ ЗАПР', 'КОНТЕНТ ЗАПР', 'КОНТЕНТ ЗАПР', 'КОНТЕНТ ЗАПР']
TEST_RECS = ['КОНТЕНТ РЕК', 'КОНТЕНТ РЕК', 'КОНТЕНТ РЕК', 'КОНТЕНТ РЕК']

def login(username: str, password: str) -> Tuple[int, str]:
    uid = dbapi.get_user_id(username, password)
    status = "OK"
    if uid == -1:
        status = "USER NOT FOUND"
    return uid, status


def get_tags(query: str) -> list[object]:
    pass

def update_userinfo(tags: list[object], uid: int = 0) -> None:
    pass

def find_by_tags(tags: list[object]) -> list[object]:
    return TEST_CONTENT

def process_query(query: str) -> list[object]:
    tags = get_tags(query)
    result = find_by_tags([])
    update_userinfo(tags)
    return result

def get_recs(uid: int = 0) -> list[object]:
    return TEST_RECS
