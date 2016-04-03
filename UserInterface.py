import json
import os
from os.path import isfile, join

import requests

auth = os.environ.get('AUTH_KEY')


def get_course():
    s = requests.Session()
    s.headers = {'Authorization': 'Bearer {0}'.format(auth)}
    r = json.loads(s.get('https://bgsu.instructure.com/api/v1/courses').text)
    s.close()

    for i in range(len(r)):
        print("[{0}] {1}".format(i + 1, r[i]['name']))

    selection = int(input("Select Course: ")) - 1

    return r[selection]['id']


def get_assignment(class_id):
    s = requests.Session()
    s.headers = {'Authorization': 'Bearer {0}'.format(auth)}
    url = 'https://bgsu.instructure.com/api/v1/courses/{0}/assignments'.format(class_id)
    params = {'bucket': 'upcoming'}
    response = json.loads(s.get(url, params=params).text)
    s.close()

    # print(response[0].keys())

    assignments = list(filter(lambda a: 'online_upload' in a['submission_types'], response))

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
