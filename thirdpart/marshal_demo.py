from datetime import datetime
from json import dumps

from flask_restful import fields
from flask_restful import marshal

serializer = {
    'InDate': fields.DateTime(dt_format="iso8601")
}


def main():
    data = {'InDate': datetime.now()}
    print(dumps(marshal(data, serializer)))

    data = {'InDate': None}
    print(dumps(marshal(data, serializer)))


if __name__ == '__main__':
    main()
