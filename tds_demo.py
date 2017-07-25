from socket import socket

from fysom import Fysom
from gevent.server import StreamServer

from tds import Parser
from tds.packets import LoginPacket
from tds.packets import PacketHeader
from tds.packets import PreLoginPacket
from tds.response import LoginResponse
from tds.tokens import Collation
from tds.tokens import Done
from tds.tokens import EnvChange
from tds.tokens import Info
from tds.tokens import LoginAck
from tds.utils import beautify_hex


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
            # message = packet.marshal()
            header = PacketHeader()
            content = header.marshal(packet)
            beautify_hex(content)
            sock.sendall(content)
        elif isinstance(packet, LoginPacket):
            response = LoginResponse()
            env1 = EnvChange()
            env1.add(1, 'CTI', 'master')
            sql_collation = Collation()
            env2 = EnvChange()
            env2.add_bytes(EnvChange.ENV_SQL_COLLATION, sql_collation.marshal())
            env3 = EnvChange()
            env3.add(EnvChange.ENV_LANGUAGE, 'us_english')
            ack = LoginAck()
            ack.program_name = "TDS"
            env = EnvChange()
            env.add(EnvChange.ENV_DATABASE, '4096', '4096')
            done = Done()
            info = Info()
            info.msg = "Changed database context to 'CTI'."
            info.server_name = 'S1DSQL04\\EHISSQL'
            info.line_number = 10

            response.add_component(env1)
            response.add_component(info)
            response.add_component(ack)
            response.add_component(env)
            response.add_component(done)

            header = PacketHeader()
            content = header.marshal(response)
            beautify_hex(content)
            sock.sendall(content)


if __name__ == '__main__':
    # parser = Parser(pre_login_request())
    # packet = parser.parse()
    # print packet.marshal()
    # parser = Parser(login_request())
    # parser.parse()
    server = StreamServer(('0.0.0.0', 1433), handle=handle)
    server.serve_forever()
