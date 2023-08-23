#!/usr/bin/python3
"""Gather data from an API"""

import requests
from sys import argv

if __name__ == '__main__':
    API_URL = 'https://jsonplaceholder.typicode.com'

    todos = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                         .format(argv[1]))
    data_user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                             .format(argv[1]))

    task_done = 0
    all_tasks = 0
    task_done_list = []

    for task in todos.json():
        all_tasks += 1
        if task['completed'] is True:
            task_done += 1
            task_done_list.append(task['title'])

    employee_name = data_user.json()['name']
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, task_done, all_tasks))

    for task in task_done_list:
        print("\t {}".format(task))
