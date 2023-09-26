#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import json
import requests
import sys
if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # request data as jSON
    user_data = requests.get(url+"users/{}".format(user_id)).json()
    username = user_data.get("username")
    todos = requests.get(url+"todos", params={"userId": user_id}).json()

    # write to json
    with open(f"{user_id}.json", "w") as json_file:
        json.dump({user_id: [{"task": t.get("title"), "completed": t.get(
            "completed"), "username": username} for t in todos]}, jsonfile)
