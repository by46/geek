from datetime import datetime

from flask import Flask
from flask import request
from werkzeug import http
from werkzeug.http import is_resource_modified

app = Flask(__name__)

ETag = "etag-v2"
LastModified = datetime(2017, 12, 28, 14, 0, 0)


@app.route("/cache")
def cache():
    if not is_resource_modified(request.environ, etag=ETag, last_modified=LastModified):
        return "", 304, {}
    headers = {
        'Last-Modified': http.http_date(datetime.utcnow()),
        'Cache-Control': 's-maxage=5',
        'ETag': ETag
    }
    return "this is a cache {0}".format(datetime.utcnow()), 200, headers


if __name__ == '__main__':
    app.run('0.0.0.0', port=8083)
