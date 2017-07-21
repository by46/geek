from socket import socket

from fysom import Fysom
from gevent.server import StreamServer

from tds import Parser
from tds.packets import PacketHeader
from tds.utils import beautify_hex
from tds.packets import LoginPacket
from tds.packets import PreLoginPacket
from tds.tokens import EnvChange
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
    while True:
        parser = Parser(sock)
        packet = parser.parse()
        if isinstance(packet, PreLoginPacket):
            packet.inst_opt = '\x00'
            message = packet.marshal()
            header = PacketHeader()
            header.packet_type = PacketHeader.TYPE_RESPONSE
            header.status = 1
            header.length = len(message) + 8
            header.pid = 1
            header.window = 0
            header.PacketID = 1
            content = header.marshal() + message
            beautify_hex(content)
            sock.sendall(content)
        elif isinstance(packet, LoginPacket):
            message = str(EnvChange())
            header = PacketHeader()
            header.packet_type = PacketHeader.TYPE_RESPONSE
            header.status = 1
            header.length = len(message) + 8
            header.pid = 1
            header.window = 0
            header.PacketID = 1
            content = header.marshal() + message
            beautify_hex(content)
            content="\x04\x01\x01\x8d\x00\xd2\x01\x00\xe3\x15\x00\x01\x03\x43\x00\x54\x00\x49\x00\x06\x6d\x00\x61\x00\x73\x00\x74\x00\x65\x00\x72\x00\xab\x70\x00\x45\x16\x00\x00\x02\x00\x22\x00\x43\x00\x68\x00\x61\x00\x6e\x00\x67\x00\x65\x00\x64\x00\x20\x00\x64\x00\x61\x00\x74\x00\x61\x00\x62\x00\x61\x00\x73\x00\x65\x00\x20\x00\x63\x00\x6f\x00\x6e\x00\x74\x00\x65\x00\x78\x00\x74\x00\x20\x00\x74\x00\x6f\x00\x20\x00\x27\x00\x43\x00\x54\x00\x49\x00\x27\x00\x2e\x00\x10\x53\x00\x31\x00\x44\x00\x53\x00\x51\x00\x4c\x00\x30\x00\x34\x00\x5c\x00\x45\x00\x48\x00\x49\x00\x53\x00\x53\x00\x51\x00\x4c\x00\x00\x01\x00\xe3\x08\x00\x07\x05\x09\x04\xd0\x00\x34\x00\xe3\x17\x00\x02\x0a\x75\x00\x73\x00\x5f\x00\x65\x00\x6e\x00\x67\x00\x6c\x00\x69\x00\x73\x00\x68\x00\x00\xab\x7a\x00\x47\x16\x00\x00\x01\x00\x27\x00\x43\x00\x68\x00\x61\x00\x6e\x00\x67\x00\x65\x00\x64\x00\x20\x00\x6c\x00\x61\x00\x6e\x00\x67\x00\x75\x00\x61\x00\x67\x00\x65\x00\x20\x00\x73\x00\x65\x00\x74\x00\x74\x00\x69\x00\x6e\x00\x67\x00\x20\x00\x74\x00\x6f\x00\x20\x00\x75\x00\x73\x00\x5f\x00\x65\x00\x6e\x00\x67\x00\x6c\x00\x69\x00\x73\x00\x68\x00\x2e\x00\x10\x53\x00\x31\x00\x44\x00\x53\x00\x51\x00\x4c\x00\x30\x00\x34\x00\x5c\x00\x45\x00\x48\x00\x49\x00\x53\x00\x53\x00\x51\x00\x4c\x00\x00\x01\x00\xad\x36\x00\x01\x71\x00\x00\x01\x16\x4d\x00\x69\x00\x63\x00\x72\x00\x6f\x00\x73\x00\x6f\x00\x66\x00\x74\x00\x20\x00\x53\x00\x51\x00\x4c\x00\x20\x00\x53\x00\x65\x00\x72\x00\x76\x00\x65\x00\x72\x00\x00\x00\x00\x00\x0c\x00\x10\x04\xe3\x13\x00\x04\x04\x34\x00\x30\x00\x39\x00\x36\x00\x04\x34\x00\x30\x00\x39\x00\x36\x00\xfd\x00\x00\x00\x00\x00\x00\x00\x00"
            sock.sendall(content)


if __name__ == '__main__':
    # parser = Parser(pre_login_request())
    # packet = parser.parse()
    # print packet.marshal()
    # parser = Parser(login_request())
    # parser.parse()
    server = StreamServer(('0.0.0.0', 1433), handle=handle)
    server.serve_forever()
