'''
To manage twisted routes
'''
import re
from liaar.lib import setting


# keep routes list
_routes = []


def add(route, name):
    '''
    Add a new route to routes list
    '''
    _routes.append((route, name))


def init():
    add('/', 'root')

    add(setting.APP_URL_FORMAT, 'app')

    add(setting.APP_URL_FORMAT +
        setting.APP_RESOURCE_URL_FORMAT, 'resource')

    add(setting.APP_URL_FORMAT +
        setting.APP_RESOURCE_URL_FORMAT +
        setting.APP_METHOD_URL_FORMAT, 'method')


def get_all():
    '''
    Get routes list
    '''
    return _routes


def extract_params(route, route_regex, path):
    '''
    Extract values and parameters from given path and return a dictionary
    '''
    params = re.findall('{([a-zA-Z0-9_]+)}', route[0])
    values = re.findall(route_regex, path)
    extracted_params = {}
    i = 0
    for param in params:
        param_value = values[0][i]
        # trim `v` character from `version` parameter
        if param == 'version':
            param_value = values[0][i].lstrip('v')

        extracted_params[param] = param_value
        i = i + 1

    return extracted_params


def get(arr_path):
    '''
    Verify and return a route with given array of postpath from twisted
    '''
    # creating the full path of the request
    path = '/' + '/'.join(arr_path)

    for route in _routes:
        route_regex = re.sub('{[a-zA-Z0-9_]+}', '([a-zA-Z0-9_]+)', route[0])
        if re.match('^' + route_regex + '$', path):
            return route, extract_params(route, route_regex, path)
            break
