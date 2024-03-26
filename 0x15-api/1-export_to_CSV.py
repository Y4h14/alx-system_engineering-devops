#!/usr/bin/python3
""" script for getting employee progress"""
from sys import argv
import requests
import csv


if __name__ == '__main__':
    user_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos\
            ".format(user_id)

    user_req = requests.get(user_url).json()
    todo_req = requests.get(todo_url).json()

    done_tasks = sum(1 for task in todo_req if task['completed'] is True)
    total_tasks = sum(1 for task in todo_req)
    file_name = "{}.csv".format(user_id)

with open(file_name, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["USER_ID", "USERNAME",
                     "TASK_COMPLETED_STATUS", "TASK_TITLE"])
    [writer.writerow([user_id, user_req['name'],
                     t.get('completed'), t.get('title')]) for t in todo_req]
