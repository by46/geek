from flask import Flask
from flask_htpasswd import HtPasswdAuth


class Pogom(Flask):
    def __init__(self, import_name, **kwargs):
        # missing some special code
        super(Pogom, self).__init__(import_name, **kwargs)


htpasswd = HtPasswdAuth()


def create_app():
    app = Pogom(__name__)
    app.config['FLASK_HTPASSWD_PATH'] = 'C:/.htpasswd'
    app.config['FLASK_SECRET'] = 'Hey Hey Kids, secure me!'
    htpasswd.init_app(app)
    return app


if __name__ == '__main__':
    app = create_app()


    # just for demonstration
    @app.route('/')
    @htpasswd.required
    def index():
        return "Hello"


    app.run()
