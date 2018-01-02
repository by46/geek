import json
from datetime import datetime

from flask_restful import fields
from flask_restful import marshal
from flask_restful.utils import unpack

if __name__ == '__main__':
    data = {'a': datetime.utcnow(), 'b': 'foo', 'person': [{
        'name': 'benjamin'
    }]}
    mfields = {'a': fields.DateTime, 'person': fields.Nested({
        'name': fields.String
    })}
    response = marshal(data, mfields)
    print('debugging ', json.dumps(response))
    value, code, header = unpack(response)
    print(value, code, header)
    x = fields.Nested({})
    print(issubclass(fields.String, type))
    xtype = type(fields.String)
    print(issubclass(xtype, (type,)))
    xtype = type(fields.String())
    print(issubclass(xtype, (type,)))
