#!/usr/bin/python3
"""Task 3"""

import json
import requests


if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com/"

    response = requests.get("{}todos".format(API_URL),
                            params={"_expand": "user"})

    if response.status_code == 200:
        data = response.json()

        dict_employed = {}

        for task in data:
            dict_employed[task["userId"]] = []

        json_filename = "todo_all_employees.json"
        with open(json_filename, mode="w", encoding="utf-8") as json_file:
            for task in data:
                dict_temp = {
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": task["user"]["username"]
                }
                dict_employed[task["userId"]].append(dict_temp)

            json.dump(dict_employed, json_file)

    else:
        print("Error: {}".format(response.status_code))
