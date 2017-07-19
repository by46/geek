import logging
import random
import time

import requests
from requests import adapters


def main(session, worker_no):
    """
    
    :param requests.Session session: 
    :param worker_no: 
    :return: 
    """
    headers = {
        'Authorization': 'bearer xIThEbkuzmbXwXyAGgUv8hVZUh8bumXV1WKpOCxv',
        'Content-Type': 'text/plain'
    }
    data = 'A' * 1024 * 1024
    url = 'http://www.newegg.online/attachment_storage/attachment/file'
    result = []
    for i in range(100):
        cur = time.time()
        content = data + str(random.randint(0, 100000))
        response = session.post(url, data=content, headers=headers)
        assert response.status_code == 200
        elapse = time.time() - cur
        logging.error('Loop %d, elapse: %s', i, elapse)
        result.append(elapse)

    return result


if __name__ == '__main__':
    sess = requests.session()
    a = adapters.HTTPAdapter()
    sess.mount('http://', a)
    elapses = main(sess, worker_no='1')
    print(sum(elapses) / len(elapses))
