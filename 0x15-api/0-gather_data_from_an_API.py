#!/usr/bin/python3
"""Python script using a REST API to return info
"""
import requests
import sys


if __name__ == "__main__":
    # my url
    base_url = "https://jsonplaceholder.typicode.com"

    # set HTTP to retrieve data
    user_data = requests.get(base_url + "/users", params={"id": sys.argv[1]})

    # retrieve a jSON and read from it
    for names in user_data.json():
        user_id = names.get("id")
        todo = requests.get(base_url + "/todos", params={"userid": user_id})

        # track tasks progress
        complete_tasks = 0
        all_tasks = []

        for tasks in todo.json():
            if tasks.get("completed") is True:
                complete_tasks += 1
                all_tasks.append(tasks.get('title'))

        # print the data
        print("Employee {:s} is done with tasks({:d}/{:d}):\n\t {}".
              format(names.get('name'), complete_tasks,
                     len(todo.json()), "\n\t".join(all_tasks)))
