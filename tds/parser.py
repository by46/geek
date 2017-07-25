import logging
from StringIO import StringIO
from socket import socket
from io import RawIOBase

from tds.packets import LoginPacket
from tds.packets import PacketHeader
from tds.request import PreLoginRequest
from tds.response import LoginResponse
from tds.tokens import Collation
from tds.tokens import Done
from tds.tokens import EnvChange
from tds.tokens import Info
from tds.tokens import LoginAckStream
from tds.tokens import PreLoginStream
from tds.utils import beautify_hex


class Parser(object):
    """
    :type conn: socket
    """
    PROCESS = {
        0x10: 'on_login',
        0x12: 'on_pre_login'
    }
    conn = None

    def __init__(self, conn):
        self.conn = conn

    def run(self):
        while True:
            header, data = self.parse_message_header()
            if header.packet_type in self.PROCESS:
                method = getattr(self, self.PROCESS.get(header.packet_type))
                method(header, data)
            else:
                logging.error('Unknown packet: %s', header.packet_type)
                self.conn.close()
                return

    def parse(self):
        """
        
        :rtype:
        """
        header, data = self.parse_message_header()
        if header.packet_type in self.PROCESS:
            method = getattr(self, self.PROCESS.get(header.packet_type))
            method(header, data)
        else:
            logging.error('Unknown packet', beautify_hex(header))
            self.conn.close()

    def parse_message_header(self):
        """
        
        :rtype: (PacketHeader, str)
        """
        header = self.conn.recv(8)
        packet_header = PacketHeader()
        packet_header.unmarshal(header)
        data = self.conn.recv(packet_header.length)
        return packet_header, StringIO(data)

    def on_pre_login(self, header, buf):
        """
        
        :param PacketHeader header: 
        :param RawIOBase buf: 
        """
        request = PreLoginRequest(buf)
        response = PreLoginStream()
        response.version = (1426128904, 0)
        response.encryption = PreLoginStream.ENCRYPT_NOT_SUP
        response.inst_opt = '\x00'
        response.thread_id = 1234
        header = PacketHeader()
        content = header.marshal(response)
        beautify_hex(content)
        self.conn.sendall(content)

    def on_login(self, header, buf):
        packet = LoginPacket()
        packet.unmarshal(buf)

        response = LoginResponse()
        env1 = EnvChange()
        env1.add(1, 'CTI', 'master')
        sql_collation = Collation()
        env2 = EnvChange()
        env2.add_bytes(EnvChange.ENV_SQL_COLLATION, sql_collation.marshal())
        env3 = EnvChange()
        env3.add(EnvChange.ENV_LANGUAGE, 'us_english')
        ack = LoginAckStream()
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
        self.conn.sendall(content)
