"""

"""
import gevent.monkey

gevent.monkey.patch_all()

from flask import Flask

app = Flask('Simple')


@app.route('/hello/demo')
def hello():
    return "<b>hello</b>"


if __name__ == '__main__':
    from gevent.pywsgi import WSGIServer

    server = WSGIServer(('0.0.0.0', 8081), application=app)
    print(app.url_map)
    server.serve_forever()
