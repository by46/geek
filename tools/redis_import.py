# -*- coding:utf-8 -*-
import logging.config
import re

import redis

# pool = redis.ConnectionPool(host="st01nbx01", port=6379, db=1)
pool = redis.ConnectionPool(host="127.0.0.1", port=6384, db=6)
r = redis.Redis(connection_pool=pool)


def get_item(content):
    return re.findall(r'<item>(.+)</item>', content)[0].strip()


def get_itemcatalog(content):
    return re.findall(r'<itemcatalog>(.+)</itemcatalog>', content)[0].strip().replace(',', '')


def deal_file_catalog(filepath):
    print "catalog"
    with open(filepath, "r") as f:
        for line in f:
            try:
                print "catalog"
                if "<item>" in line:
                    item = get_item(line)
                if "<itemcatalog>" in line:
                    catalog = get_itemcatalog(line)
                    r.hset(item, "catalog", catalog)
                    # r.set("c_"+item, catalog)
                    r.sadd("Catalog", catalog)
                    r.sadd(catalog, item)
            except Exception as e:
                with open("log/log_catalog.txt", "a") as log:
                    log.write("debug:" + str(e) + "line: " + line + "\n")


# deal_file_catalog("data/itemcatalog.xml")


config = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
        'file_handler': {
            'level': 'DEBUG',
            'filename': 'title.log',
            'class': 'logging.FileHandler',
            'formatter': 'standard'
        }
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file_handler'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}
logging.config.dictConfig(config)

import gevent
from gevent.queue import Queue
from gevent.queue import Empty


class Importer(object):
    def __init__(self, xml_path, workers=4):
        self.xml_path = xml_path
        self.workers = workers
        self.tasks = Queue()
        self.stop = False

    def run(self):
        logging.info("Import starter")
        workers = [gevent.spawn(self.worker, i) for i in range(self.workers)]
        for i in range(100):
            self.tasks.put("item {0}".format(i))
        gevent.joinall(workers)

    def worker(self, n):
        logging.debug("worker %s is ready", n)
        tasks = self.tasks
        while True:
            if tasks.empty() and self.stop:
                logging.debug("worker %s is stop", n)
                return

            try:
                task = self.tasks.get(block=False)
            except Empty:
                logging.debug("queue is Empty")
                gevent.sleep(1)
                continue
            logging.debug("worker %s is processing", n)


if __name__ == '__main__':
    importer = Importer("items.xml")
    importer.run()
