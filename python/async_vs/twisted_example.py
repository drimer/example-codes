from twisted.internet import reactor
from twisted.web import server, resource


class Simple(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        reactor.callLater(5, self._process_get, request)
        return server.NOT_DONE_YET

    def _process_get(self, request):
        q_args = request.args.get(b'q')
        if q_args:
            get_param = q_args[0].decode('utf-8')
            response_html = "<html>{} is here</html>".format(get_param).encode(
                'utf-8')
        else:
            response_html = "<html>Not found</html>".encode('utf-8')

        request.write(response_html)
        request.finish()


site = server.Site(Simple())
reactor.listenTCP(2001, site)
reactor.run()
