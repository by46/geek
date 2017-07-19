import logging
import time

from flask import Flask
from gevent.pywsgi import WSGIServer


def create_app():
    app = Flask(__name__)

    @app.route('/hello/file/')
    def index():
        return 'hello'

    return app


class DemoMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        cur = time.time()
        response = self.app(environ, start_response)
        logging.error('elapse  %s', time.time() - cur)
        return response


if __name__ == '__main__':
    application = create_app()
    middleware = DemoMiddleware(application)
    WSGIServer(('', 8080), application=middleware).serve_forever()
