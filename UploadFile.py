from os.path import getsize

def upload_file(class_id, assign_id, file_name):
    domain = 'https://bgsu.instructure.com'
    upload_path = '/api/v1/courses/{0}/assignments/{1}/submissions/self/files'.format(class_id, assign_id)
    data = {'name': file_name, 'size': getsize(file_name)}
    url = domain + upload_path

    print(url, file_name)