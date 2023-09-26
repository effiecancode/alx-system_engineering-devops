#!/usr/bin/python3
"""Python script Gather data from an API
"""
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    base_url = "https://jsonplaceholder.typicode.com"
    user_info_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_info_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data.get("name")
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task["completed"]]

    print(f"Employee {employee_name} is done with tasks"
          f"({len(completed_tasks)}/({total_tasks}):")

    for task in completed_tasks:
        print(f"{task['title']}")
