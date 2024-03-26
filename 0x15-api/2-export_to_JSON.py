#!/usr/bin/python3
""" script for creating a json file of the data"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos\
            ".format(user_id)

    user_req = requests.get(user_url).json()
    todo_req = requests.get(todo_url).json()

    done_tasks = sum(1 for task in todo_req if task['completed'] is True)
    total_tasks = sum(1 for task in todo_req)
    filename = "{}.json".format(user_id)
    with open(filename, 'w') as f:
        json.dump({user_id: [{
            "task": t.get('title'),
            "completed": t.get('completed'),
            "username": user_req['username']
            } for t in todo_req]}, f)
