#!/usr/bin/python3
"""Python script that, using this REST API"""

import requests
import json
import sys


users = requests.get('https://jsonplaceholder.typicode.com/users').json()
"""Get the users response in json format"""

tasks = {}

for user in users:
    user_id = user.get('id')
    username = user.get('username')

    todo_list = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={user_id}').json()

    tasks_list = [{'username': username, 'task': task.get(
                   'title'), 'completed': task.get('completed')} for task in todo_list]

    tasks[user_id] = tasks_list

with open('todo_all_employees.json', 'w') as jsonfile:
    json.dump(tasks, jsonfile)

if __name__ == '__main__':
    pass
