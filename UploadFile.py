from collections import OrderedDict
from os.path import getsize

import requests

import config


def upload_file(class_id, assign_id, file_name):
    # Create a session with authentication header
    auth_session = requests.Session()
    auth_session.headers = {'Authorization': 'Bearer {0}'.format(config.auth_token)}

    # Get file upload parameters from Canvas
    try:
        path = '/api/v1/courses/{0}/assignments/{1}/submissions/self/files'.format(class_id, assign_id)
        data = OrderedDict({'name': file_name, 'size': getsize(file_name)})
        url = ''.join([config.domain, path])
        response = auth_session.post(url, data)
        response.raise_for_status()
    finally:
        auth_session.close()

    # Using upload parameters and url retrieved by last step, upload file to canvas
    # `auth_session` is not used here because all authentication is in params
    try:
        data = OrderedDict(response.json()['upload_params'])
        # data['file'] = open(file_name, 'rb')
        url = response.json()['upload_url']
        response = requests.post(url, data=data, files={'file': open(file_name, 'rb')})
        response.raise_for_status()
    finally:
        response.close()

    # Using file id from the last step, submit the assignment
    try:
        file_id = response.json()['id']
        url = ''.join([config.domain, '/api/v1/courses/{0}/assignments/{1}/submissions'.format(class_id, assign_id)])
        data = {'submission[submission_type]': 'online_upload', 'submission[file_ids][]': file_id}
        response = auth_session.post(url, data=data)
        response.raise_for_status()
    finally:
        response.close()
