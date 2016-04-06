import os
from collections import OrderedDict
from os.path import getsize

import requests

auth = os.environ.get('AUTH_KEY')


def upload_file(class_id, assign_id, file_name):
    domain = 'https://bgsu.instructure.com'
    upload_path = '/api/v1/courses/{0}/assignments/{1}/submissions/self/files'.format(class_id, assign_id)
    data = OrderedDict({'name': file_name, 'size': getsize(file_name)})
    url = ''.join([domain, upload_path])

    s = requests.Session()
    s.headers = {'Authorization': 'Bearer {0}'.format(auth)}
    try:
        response = s.post(url, data).json()
    finally:
        s.close()

    upload_url = response['upload_url']
    upload_params = OrderedDict()

    for key in response['upload_params'].keys():
        upload_params[key] = response['upload_params'][key]

    upload_params['file'] = ''.join(['@', file_name])

    # print(upload_url, upload_params)

    upload_response = requests.post(upload_url, data=upload_params, files={file_name: open(file_name, 'rb')})
    upload_response.raise_for_status()
    upload_response.close()

    file_id = upload_response.json()['id']
    submit_url = ''.join([domain, '/api/v1/courses/{0}/assignments/{1}/submissions'.format(class_id, assign_id)])

    submit_data = {'submission[submission_type]': 'online_upload', 'submission[file_ids][]': file_id}
    submit_response = requests.post(submit_url, data=submit_data, headers={'Authorization': 'Bearer {0}'.format(auth)})
    submit_response.raise_for_status()
    submit_response.close()
