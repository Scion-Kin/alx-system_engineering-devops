#!/usr/bin/python3
''' This script returns information about all employees' TODO
list progress and saves it to a json file '''

import json
import requests
import sys


if __name__ == '__main__':

    response = requests.get('https://jsonplaceholder.typicode.com/todos/')

    all_data = response.json()

    all_users = []
    for i in all_data:
        if i['userId'] not in all_users:
            all_users.append(i['userId'])

    with open('todo_all_employees.json', 'w') as file:

        data = {}
        for i in all_users:
            employee = requests.get(
                'https://jsonplaceholder.typicode.com/users/{}'.format(i))
            employee = employee.json()
            name = employee['username']

            temp = []
            for j in all_data:
                if j['userId'] == i:
                    user_data = {"username": name,
                                 "task": j['title'],
                                 "completed": j['completed']}

                    temp.append(user_data)
            data[i] = temp

        json.dump(data, file)
