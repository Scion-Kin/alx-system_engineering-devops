#!/usr/bin/python3
''' This module returns information about his/her TODO
list progress for a given employee ID. '''

import requests
import sys


if __name__ == '__main__' and sys.argv[1]:

    response = requests.get('https://jsonplaceholder.typicode.com/todos/')

    id = int(sys.argv[1])
    all_data = response.json()
    count = 0
    total_tasks = 0
    tasks = []
    for i in all_data:
        if i['userId'] == id:
            total_tasks = total_tasks + 1

        if i['userId'] == id and i['completed']:
            count = count + 1

            tasks.append(i['title'])

    employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(id))
    employee = employee.json()
    name = employee['name']

    print('Employee {} is done with tasks({}/{}):'.format(
        name, count, total_tasks))

    for i in tasks:
        print(f"\t {i}")
