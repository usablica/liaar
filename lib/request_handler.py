'''
Twisted request handlers
'''
from lib import app, exception


def method(request, route_params):
    try:
        method_json = app.get_method(route_params['app_name'],
                                     route_params['version'],
                                     route_params['resource_name'],
                                     route_params['method_name'])
    except KeyError:
        exception.handle('No method found')

    return '%s' % method_json
