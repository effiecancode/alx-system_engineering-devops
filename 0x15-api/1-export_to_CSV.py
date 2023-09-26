#!/usr/bin/python3
"""Exports to-do list to CSV format."""
import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # send HTTP request that retrieves data as JSON
    user_info = requests.get(url + "users/{}".format(user_id)).json()
    username = user_info.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # write to csv using the csv module
    with open(f"{user_id}.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
        ) for t in todos]
