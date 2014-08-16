'''
Twisted request handlers
'''
from liaar.lib import app, parser
import json


def method(request, route_params):
    # set response content-type to json
    request.responseHeaders.addRawHeader(b"content-type", b"application/json")
    method_setting = app.get_method(route_params['app_name'],
                                    route_params['version'],
                                    route_params['resource_name'],
                                    route_params['method_name'])

    return json.dumps(parser.parse_param(method_setting))
