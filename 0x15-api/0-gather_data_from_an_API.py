#!/usr/bin/python3
"""Python script using a REST API to return info
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    else:
        employee_id = int(sys.argv[1])

    # my urls
    base_url = "https://jsonplaceholder.typicode.com"
    user_info = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userid={employee_id}"

    # set HTTP to retrieve data
    user_response = requests.get(user_info)
    todos_response = requests.get(todos_url)

    # return retrieved data as JSON /data parsing/
    user_data = user_response.json()
    todos_data = todos_response.json()

    # fetch from the json
    employee_name = user_data.get("name")
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task["completed"]]

    # print the retrieved data
    print(f"Employee {employee_name} is done with tasks "
          f"({len(completed_tasks)}/{total_tasks}):")
    # print(f"\t{user_data['name']}")

    for task in completed_tasks:
        print(f"\t {task['title']}")
