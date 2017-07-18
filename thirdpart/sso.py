import gevent.monkey

gevent.monkey.patch_all()
import logging
import random
import time

import gevent
import requests
import requests.adapters

def main(session, worker_no):
    url = 'http://172.16.171.23:8212/ll-user-management/v1/account/user'
    value = "Bearer xIThEbkuzmbXwXyAGgUv8hVZUh8bumXV1WKpOCxv"
    headers = {
        'Authorization': value,
        'X-Newkit-Token': value
    }
    while True:
        response = session.get(url, headers=headers)
        logging.error('%d, %d %s', worker_no, time.time(), response.status_code)
        assert response.status_code == 200
        interval = random.randint(1, 5)
        logging.error('%d sleep %ss', worker_no, interval)
        time.sleep(interval)


if __name__ == '__main__':
    session = requests.session()
    # adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=20)
    # session.mount('http://', adapter)
    workers = []
    gevent.joinall([gevent.spawn(main, session, i) for i in range(1)])
