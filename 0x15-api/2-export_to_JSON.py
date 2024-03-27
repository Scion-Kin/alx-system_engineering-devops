#!/usr/bin/python3
''' This module returns information about an employees' TODO
list progress for a given employee ID and saves to a json file '''

import json
import requests
import sys


if __name__ == '__main__' and sys.argv[1]:

    response = requests.get('https://jsonplaceholder.typicode.com/todos/')

    id = int(sys.argv[1])
    all_data = response.json()
    tasks = []

    with open(f'{id}.json', 'w') as file:
        temp = {id: []}
        for i in all_data:
            if i['userId'] == id:

                data = {"task": i['title'], "completed": i['completed']}

                temp[id].append(data)

        json.dump(temp, file)
