#!/usr/bin/python3
""" Creates a CSV file of the data"""
import csv
import requests
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos\
            ".format(user_id)

    user_req = requests.get(user_url).json()
    todo_req = requests.get(todo_url).json()

    file_name = "{}.csv".format(user_id)

    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME",
                         "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        [writer.writerow([user_id, user_req['username'],
                          t.get('completed'),
                          t.get('title')]) for t in todo_req]
