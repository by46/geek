"""
demonstrate metaclass sample
"""
from six import add_metaclass


def decorator(fn):
    def wrapped(self):
        print('in wrapped')
        return fn(self)

    return wrapped


def get(self):
    print('{0:s} in {1:s}'.format('get', self))


class Meta(type):
    def __new__(cls, name, bases, attributes):
        attributes['get'] = decorator(get)
        return type(name, bases, attributes)


@add_metaclass(Meta)
class MyClass(object):
    serialize_class = object


if __name__ == '__main__':
    x = MyClass()
    x.get()
