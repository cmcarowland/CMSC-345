import json
import os

def get_users():
    users = {}
    if os.path.exists('users.txt'):
        with open('users.txt', 'r') as iFile:
            users = json.load(iFile)

    return users

def save_users(users : dict[str, str]):
    with open('users.txt', 'w') as iFile:
        json.dump(users, iFile)