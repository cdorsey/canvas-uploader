# Canvas Uploader #

Provides a command-line interface for students to submit file upload assignments to Instructure Canvas

## Requirements ##

- Python 3.5
- [Requests library](https://pypi.python.org/pypi/requests)
- config.py file (Info below)

## Configuration ##

In order to function, a file named config.py must be present in the same folder as main.py, following the following format:

    auth_token = 'Canvas Bearer token here' # More info below
    domain = 'https://your-schools-domain.instructure.com'

[How to obtain a bearer token.](https://canvas.instructure.com/doc/api/file.oauth.html#manual-token-generation) ** Do not share this key with others. **

## Usage ##

To use this application, put the file you want to upload in the same folder as `main.py`, and run the command `python main.py`. You will then be walked through selecting a course and assignment, and the file you want to upload.

## License ##

This code is distributed under the MIT License. See LICENSE for more information. 