from typing import Tuple
import requests
import config

config.read_config()

addr = config.get_param_value('engineaddr')
port = config.get_param_value('engineport')

def get_recs(uid: int):
    return requests.post(
        f'http://{addr}:{port}/recs',
        json={
            'uid': uid
        }
    ).json()


def get_ctx_for_query(query: str, uid: str):
    response = requests.post(
        f'http://{addr}:{port}/find',
        json={
            'uid': uid,
            'q': query
        }
    )
    return response.json()


def login(username: str, password: str) -> Tuple[int, bool]:
    response = requests.post(
        f'http://{addr}:{port}/login',
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
        f'http://{addr}:{port}/register',
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

def get_username(uid: int) -> str:
    response = requests.post(
        f'http://{addr}:{port}/get_user',
        json={
            'uid': uid
        }
    ).json()
    return f"{response['name']} {response['surname'][0]}."
