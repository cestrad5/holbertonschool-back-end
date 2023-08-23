#!/usr/bin/python3
""" Task 0 """


if __name__ == '__main__':
    import requests
    import sys

    if len(sys.argv) != 2:
        print("Enter a valid number")
        sys.exit()

    taskId = sys.argv[1]

    userTasks = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{taskId}/todos').json()
    userInfo = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{taskId}').json()

    userName = userInfo.get('name')
    completedTasks = [todo for todo in userTasks if todo['completed']]
    print(f"Employee {userName} is done with"
          f" tasks({len(completedTasks)}/{len(userTasks)}):")
    for task in completedTasks:
        print(f"\t {task.get('title')}")
