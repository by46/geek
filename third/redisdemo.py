import json

import redis
import requests

if __name__ == '__main__':
    client = redis.StrictRedis(host='10.16.75.12', port=12345, db=0)
    token = client.get('1498634437752')
    user = json.loads(token)
    print(json.dumps(user, indent=True))

    lst = ['xxx', 'data']
    request(*lst)

def request(url, data):
    params = dict()
    if isinstance(data, (dict, tuple, list)):
        params['json'] = data
    else:
        params['data'] = data
    requests.post(url, **params)
    requests.post(url, json='', )
    pass
