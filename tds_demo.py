import gevent.monkey

# gevent.monkey.patch_all()
import logging
from socket import socket

from fysom import Fysom
from gevent.server import StreamServer

from tds import Parser


def handle(sock, address):
    """
    
    :param socket sock: 
    :param address: 
    :return: 
    """
    state = Fysom(initial='init',
                  events=[
                      {'name': 'pre_login', 'src': 'init', 'dst': 'pre_login'},
                      {'name': 'login', 'src': 'pre_login', 'dst': 'login'},
                      {'name': 'batch', 'src': 'login', 'dst': 'batch'},
                      {'name': 'batch', 'src': 'batch', 'dst': 'batch'},
                      {'name': 'stop', 'src': 'batch', 'dst': 'stop'},
                      {'name': 'stop', 'src': 'init', 'dst': 'stop'},
                      {'name': 'stop', 'src': 'pre_login', 'dst': 'stop'},
                      {'name': 'stop', 'src': 'login', 'dst': 'stop'},
                  ])
    logging.error('address %s', address)
    parser = Parser(sock)
    parser.run()


if __name__ == '__main__':
    # parser = Parser(pre_login_request())
    # packet = parser.parse()
    # print packet.marshal()
    # parser = Parser(login_request())
    # parser.parse()
    server = StreamServer(('0.0.0.0', 1433), handle=handle)
    server.serve_forever()
