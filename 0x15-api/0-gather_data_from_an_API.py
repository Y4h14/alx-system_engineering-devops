#!/usr/bin/python3
""" script for getting employee progress"""
import requests
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos\
            ".format(user_id)

    user_req = requests.get(user_url).json()
    todo_req = requests.get(todo_url).json()

    print("Employee {} is done with".format(user_req['name']), end='')
    done_tasks = sum(1 for task in todo_req if task['completed'] is True)
    total_tasks = sum(1 for task in todo_req)

    print(" tasks({}/{}):".format(done_tasks, total_tasks))

    for task in todo_req:
        if task['completed'] is True:
            print("\t {}".format(task['title']))
