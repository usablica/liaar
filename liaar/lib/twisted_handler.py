'''
Handle twisted resources and routing
'''
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
from liaar.lib import route, exception, logger, setting, request_handler
import json


class SiteResource(Resource):
    isLeaf = True

    def render_GET(self, request):
        logger.info('Processing request for %s' % request.path)
        route_item = route.get(request.postpath)

        if route_item is None:
            exception.handle('No route found for: %s' % request.path)

        route_object, route_params = route_item

        # set route name
        route_name = route_object[1]

        if route_name == 'root':
            return 'root'
        elif route_name == 'app':
            return 'app: %s' % route_params
        elif route_name == 'resource':
            return 'resource'
        elif route_name == 'method':
            return request_handler.method(request, route_params)

def start():
    root = SiteResource()
    factory = Site(root)
    reactor.listenTCP(setting.LIAAR_PORT, factory)
    logger.info('Liaar is available on port %d' % setting.LIAAR_PORT)
    # run the twisted
    reactor.run()
