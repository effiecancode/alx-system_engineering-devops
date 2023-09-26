#!/usr/bin/python3
"""Exports to-do list to JSON format"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users_data = requests.get(url + "users").json()

    todo_dict = {}

    # iterate to gather task info and put it in a list
    for user in users_data:
        user_id = user.get("id")
        tasks = requests.get(url + "todos", params={"userId": user_id}).json()
        user_tasks = [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        } for task in tasks]

        # data is stored in this dict, with userid as the key
        todo_dict[user_id] = user_tasks

    # Write into JSON
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(todo_dict, jsonfile)
