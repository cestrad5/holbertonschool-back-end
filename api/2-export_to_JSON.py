#!/usr/bin/python3
"""Task 2"""


import json
import requests
from sys import argv


if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com/"

    user_id = argv[1]
    response = requests.get("{}users/{}/todos".format(API_URL, user_id),
                            params={"_expand": "user"})

    if response.status_code == 200:
        data = response.json()

        dict_employed = {user_id: []}

        json_filename = "{}.json".format(user_id)
        with open(json_filename, mode="w", encoding="utf-8") as json_file:
            for task in data:
                dict_temp = {
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": task["user"]["username"]
                }
                dict_employed[user_id].append(dict_temp)

            json.dump(dict_employed, json_file)
            print("{}".format(response.status_code))
    else:
        print("Error: {}".format(response.status_code))

