'''
Twisted request handlers
'''
from lib import parser, path


def method(request, route_params):
    method_filename = path.get_method_filename(route_params['app_name'],
                                               route_params['resource_name'],
                                               route_params['method_name'])
    method_json = parser.load_and_parse(method_filename)
    return '%s' % method_json
