# import model_api

# TEST_CONTENT = ['КОНТЕНТ ЗАПР', 'КОНТЕНТ ЗАПР', 'КОНТЕНТ ЗАПР', 'КОНТЕНТ ЗАПР']

# def get_content_for_query(query: str) -> list[object]:
#     model_api.find(query) # обработка запроса пользователя
#     return TEST_CONTENT # временно

# def get_content_for_recs() -> list[object]:
#     return ['КОНТЕНТ РЕК', 'КОНТЕНТ РЕК', 'КОНТЕНТ РЕК', 'КОНТЕНТ РЕК']

from typing import Tuple
import requests

def get_recs():
    response = requests.get('http://192.168.1.78:5001/recs')
    return response.json()

def get_ctx_for_query(query: str):
    response = requests.post(
        'http://192.168.1.78:5001/find',
        json={
            'uid': '0',
            'q': query
        }
    )
    return response.json()

def login(username: str, password: str) -> Tuple[int, bool]:
    response = requests.post(
        'http://192.168.1.78:5001/login',
        json={
            'username': username,
            'password': password
        }
    ).json()
    if response['status'] == 'USER NOT FOUND':
        return 0, False
    return response['uid'], True

def register(username: str, surname: str, name: str, number: str, email: str, password: str) -> Tuple[int, bool]:
    response = requests.post(
        'http://192.168.1.78:5001/register',
        json={
            'username': username,
            'surname': surname,
            'name': name,
            'number': number,
            'email': email,
            'password': password
        }
    ).json()
    if response['status'] == 'LOGIN ALREADY TAKEN':
        return 0, False
    return response['uid'], True