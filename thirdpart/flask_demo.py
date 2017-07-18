import logging

from flask import Flask
from flask import request
from gevent.pywsgi import WSGIServer


def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['POST'])
    def upload():
        logging.error('coming')
        chunk_size = 1024 * 4
        stream = request.stream  # type: io.IOBase
        with open('file.dat', 'wb') as writer:
            while True:
                content = stream.read(chunk_size)
                logging.error('read data: %d', len(content))
                if not content:
                    break
                writer.write(content)
        return ''

    return app


if __name__ == '__main__':
    from werkzeug.contrib.profiler import ProfilerMiddleware

    application = create_app()
    application = ProfilerMiddleware(application)
    WSGIServer(('', 8080), application=application).serve_forever()
