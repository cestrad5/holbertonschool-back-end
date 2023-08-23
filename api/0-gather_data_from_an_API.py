#!/usr/bin/python3
"""Gather data from an API"""

import requests
from sys import argv

if __name__ == '__main__':
    API_URL = 'https://jsonplaceholder.typicode.com'

    user_id = argv[1]
    response = \
        requests.get(
            f'{API_URL}/users/{user_id}/todos',
            params={'_expand': 'user'}
        )

    if response.status_code == 200:
        data = response.json()
        EMPLOYEE_NAME = data[0]['user']['EMPLOYEE_NAME']
        tasks_done = [task for task in data if task['completed']]
        NUMBER_OF_DONE_TASKS = len(tasks_done)
        TOTAL_NUMBER_OF_TASKS = len(data)

        first_str = f"Employee {EMPLOYEE_NAME} is done with tasks"

        print(f"{first_str}({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
        for task in tasks_done:
            print(f"\t {task['title']}")
    else:
        print(f"Error: {response.status_code}")
