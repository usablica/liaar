'''
Handle twisted resources and routing
'''
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
from lib import route, exception


class SiteResource(Resource):
    isLeaf = True

    def render_GET(self, request):
        route_item = route.get(request.postpath)

        if route_item is None:
            exception.handle('No route found for this URL.')

        route_name = route_item[0][1]
        route_param = route_item[1]

        if route_name == 'root':
            return 'root'
        elif route_name == 'app':
            return 'app: %s' % route_param
        elif route_name == 'resource':
            return 'resource'
        elif route_name == 'method':
            return 'method'
        else:
            return "<html><body><pre>%s</pre></body></html>" % (request.prepath,)


def start():
    root = SiteResource()
    factory = Site(root)
    reactor.listenTCP(8880, factory)
    reactor.run()
