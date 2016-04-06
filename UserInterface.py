import os
from os.path import isfile

import requests

import config

# Create module-wide authenticated session
auth_session = requests.Session()
auth_session.headers = {'Authorization': 'Bearer {0}'.format(config.auth_token)}


def get_course():
    try:
        response = auth_session.get(''.join([config.domain, '/api/v1/courses']))
    finally:
        auth_session.close()

    for i in range(len(response.json())):
        print("[{0}] {1}".format(i + 1, response.json()[i]['name']))

    selection = int(input("Select Course: ")) - 1

    return response.json()[selection]['id']


def get_assignment(class_id):
    url = ''.join([config.domain, '/api/v1/courses/{0}/assignments'.format(class_id)])
    # params = {'bucket': 'upcoming'}
    params = {'per_page': 30}
    try:
        response = auth_session.get(url, params=params)
    finally:
        auth_session.close()

    assignments = list(filter(lambda a: 'online_upload' in a['submission_types'], response.json()))

    print()
    for i in range(len(assignments)):
        print("[{0}] {1}".format(i + 1, assignments[i]['name']))

    selection = int(input("Select assignment: ")) - 1

    return assignments[selection]['id']


def get_file():
    files = list(filter(lambda f: isfile(f), os.listdir('.')))

    print()
    for i in range(len(files)):
        print("[{0}] {1}".format(i + 1, files[i]))

    selection = int(input("Select file: ")) - 1

    return files[selection]
