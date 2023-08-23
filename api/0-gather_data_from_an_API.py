#!/usr/bin/python3
"""Task 0"""
import sys
import requests


def fetch_user_info(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"

    response = requests.get(user_url)
    user_info = response.json()

    return user_info


def fetch_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    response = requests.get(todo_url)
    todo_list = response.json()

    total_tasks = len(todo_list)
    completed_tasks = sum(task['completed'] for task in todo_list)

    return completed_tasks, total_tasks, todo_list


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        return

    employee_id = int(sys.argv[1])

    try:
        user_info = fetch_user_info(employee_id)
        employee_name = user_info['name']
    except KeyError:
        print(f"Employee with ID {employee_id} not found.")
        return

    completed_tasks, total_tasks, todo_list = fetch_employee_todo_progress(
        employee_id)

    print(
        f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

    for task in todo_list:
        if task['completed']:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    main()
