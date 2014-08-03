'''
To parse json files inside applications (setting.json, resource etc.)
'''

import json
from faker import Factory
from liaar.lib import exception


def load_and_parse(filename):
    '''
    Load and parse JSON file
    '''
    with open(filename, 'r') as f:
        try:
            return json.load(f)
        except ValueError as detail:
            exception.handle('Failed to parse the JSON.', detail)


def parse_param(value):
    '''
    Parse resources JSON setting file parameters
    '''

    formatter_name = None
    is_list = False
    list_count = 10

    # if the value is a string (single value)
    if isinstance(value, basestring):
        formatter_name = value
    # or if it's a list
    elif isinstance(value, dict):
        if 'formatter' in value:
            formatter_name = value['formatter']
        if 'type' in value:
            is_list = True
        if 'count' in value:
            list_count = value['count']
    else:
        exception.handle('Unknown resource property: %s' % value)

    if formatter_name is None:
        exception.handle('Formatter is empty: %s' % value)

    # ok let's execute the function
    try:
        faker = Factory.create()

        if not is_list:
            return faker.__getattribute__(formatter_name)()
        else:
            list_output = []
            for i in range(list_count):
                list_output.append(faker.__getattribute__(formatter_name)())

            return list_output
    except AttributeError:
        exception.handle('Can\'t parse resource\'s property: %s' % value)
