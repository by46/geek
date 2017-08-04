from gevent import socket
from geventconnpool import ConnectionPool


class MyPool(ConnectionPool):
    def _new_connection(self):
        return socket.create_connection(("www.baidu.com", 80))


if __name__ == '__main__':
    pool = MyPool(20)
    with pool.get() as conn:
        conn.send("PING\n")
