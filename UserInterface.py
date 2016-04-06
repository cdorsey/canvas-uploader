import os
from os.path import isfile

import requests

auth = os.environ.get('AUTH_KEY')


def get_course():
    s = requests.Session()
    s.headers = {'Authorization': 'Bearer {0}'.format(auth)}
    try:
        response = s.get('https://bgsu.instructure.com/api/v1/courses').json()
    finally:
        s.close()

    for i in range(len(response)):
        print("[{0}] {1}".format(i + 1, response[i]['name']))

    selection = int(input("Select Course: ")) - 1

    return response[selection]['id']


def get_assignment(class_id):
    s = requests.Session()
    s.headers = {'Authorization': 'Bearer {0}'.format(auth)}
    url = 'https://bgsu.instructure.com/api/v1/courses/{0}/assignments'.format(class_id)
    # params = {'bucket': 'upcoming'}
    params = {'per_page': 30}
    try:
        response = s.get(url, params=params).json()
    finally:
        s.close()

    # print(response[0].keys())

    assignments = list(filter(lambda a: 'online_upload' in a['submission_types'], response))
    # assignments = response

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
