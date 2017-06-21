"""Modify function's doc

"""

import inspect
from functools import wraps

from requests import Session


def wrap_session(fn):
    default_session = Session()
    doc = inspect.getdoc(fn)
    doc = '\n'.join([x for x in doc.split('\n') if not x.startswith(':param session')])
    fn.__doc__ = doc

    @wraps(fn)
    def decorator(*args, **kwargs):
        kwargs['session'] = default_session
        return fn(*args, **kwargs)

    return decorator


@wrap_session
def send_http(url, method='GET', session=None):
    """send http with requests

    :param url:
    :param method:
    :param session:
    :return:
    """
    print(url, method, session)


if __name__ == '__main__':
    send_http('http://www.newegg.com')
    print(send_http.__doc__)
