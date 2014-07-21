'''
To parse json files inside applications (setting.json, resource etc.)
'''

import json
from lib import exception


def load_and_parse(filename):
    '''
    Load and parse JSON file
    '''
    with open(filename, 'r') as f:
        try:
            return json.load(f)
        except ValueError as detail:
            exception.handle('Failed to parse the JSON.', detail)
