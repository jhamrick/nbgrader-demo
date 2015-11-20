import tornado
from notebook.utils import url_path_join as ujoin


class ProxyHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def forward(self, path):
        body = None if self.request.body == b'' else self.request.body
        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch(
            ujoin('http://localhost:5000', path),
            method=self.request.method,
            body=body,
            headers=self.request.headers,
            follow_redirects=True,
            callback=self.callback)

    def get(self, path):
        return self.forward(path)

    def put(self, path):
        return self.forward(path)

    def post(self, path):
        return self.forward(path)

    def callback(self, request):
        self.finish(request.body)


default_handlers = [
    (r"/formgrader/(?P<path>.*)", ProxyHandler)
]

def load_jupyter_server_extension(nbapp):
    """Load the nbserver"""
    webapp = nbapp.web_app
    base_url = webapp.settings['base_url']
    webapp.add_handlers(".*$", [
        (ujoin(base_url, pat), handler)
        for pat, handler in default_handlers
    ])
