#!/usr/bin/python3
"""Python script using a REST API to return info
"""
import requests
import sys

if __name__ == "__main__":

    def get_employee_todo_progress(employee_id):
        """
        function that takes employee_id (must be an int) as parameter
        and returns employee todos progress
        """
        base_url = "https://jsonplaceholder.typicode.com"
        user_info_url = f"{base_url}/users/{employee_id}"
        todos_url = f"{base_url}/todos?userId={employee_id}"

        user_response = requests.get(user_info_url)
        todos_response = requests.get(todos_url)
        if (user_response.status_code != 200 or
                todos_response.status_code != 200):
            return

        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_data.get("name")
        total_tasks = len(todos_data)
        completed_tasks = [task for task in todos_data if task["completed"]]

        print(f"Employee {employee_id} is done with tasks "
              f"({len(completed_tasks)}/({total_tasks}):")
        print(f"EMLOYEE_NAME: {employee_name}")
        print(f"NUMBER_OF_DONE_TASKS: {len(completed_tasks)}")
        print(f"TOTAL_NUMBER_OF_TASKS: {total_tasks}")

        for task in completed_tasks:
            print(f"{task['title']}")

        # if len(sys.argv) != 2:
        #     print("Provide id as command line argument")
        # else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
