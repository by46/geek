from werkzeug.routing import Map
from werkzeug.routing import Rule
from werkzeug.routing import Subdomain


def main():
    m = Map([
        Rule('/', endpoint='static/index'),
        Rule('/about', endpoint='static/about'),
        Rule('/help', endpoint='static/help'),
        Subdomain('kb', [
            Rule('/', endpoint='kb/index'),
            Rule('/browse', endpoint='kb/browse'),
            Rule('/browse/<int:id>/', endpoint='kb/browse'),
            Rule('/browse/<int:id>/<int:page>', endpoint='kb/browse'),
        ])
    ], default_subdomain='www')
    c = m.bind('example.com')
    print c.build('kb/browse', dict(id=42))
    print c.build('kb/browse')
    print c.build('kb/browse', dict(id=42, page=3))
    print c.build('static/about')
    print c.build('static/about', force_external=True)

    c = m.bind('example.com', '/applications/example')
    print c.build('kb/browse', dict(id=42))
    c = m.bind('example.com', '/applications/example')
    print c.build('kb/browse', dict(id=42))

    print c.match('/')
    print c.match('/about')
    c = m.bind('example.com', '/', 'kb')
    print c.match('/')
    print c.match("/browse/42/23")
    # print c.match("/browse/42/23/")
    from pprint import pformat
    print repr(m), pformat(list([Rule('/', endpoint='files'), Rule('/', endpoint='files')]), width=30)


if __name__ == '__main__':
    main()
