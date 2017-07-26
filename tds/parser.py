import logging
from io import BytesIO
from socket import socket
from time import time

from tds.packets import PacketHeader
from tds.pool import get_connection
from tds.request import LoginRequest
from tds.request import PreLoginRequest
from tds.request import SQLBatchRequest
from tds.response import LoginResponse
from tds.tokens import Collation
from tds.tokens import Done
from tds.tokens import EnvChange
from tds.tokens import Info
from tds.tokens import LoginAckStream
from tds.tokens import PreLoginStream

db_conn = get_connection()


class Parser(object):
    """
    :type conn: socket
    """
    PROCESS = {
        0x01: 'on_batch',
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
                self.on_transfer(header, data)

    def parse_message_header(self, conn=None):
        """
        :param socket conn:
        :rtype: (PacketHeader, BytesIO)
        """
        conn = conn or self.conn
        header = conn.recv(8)
        packet_header = PacketHeader()
        packet_header.unmarshal(header)
        length = packet_header.length - 8
        data = None
        if length:
            data = conn.recv(length)
        return packet_header, BytesIO(data)

    def on_pre_login(self, header, buf):
        """
        
        :param PacketHeader header: 
        :param BytesIO buf: 
        """
        request = PreLoginRequest(buf)
        response = PreLoginStream()
        response.version = (1426128904, 0)
        response.encryption = PreLoginStream.ENCRYPT_NOT_SUP
        response.inst_opt = ''
        response.thread_id = 1234
        header = PacketHeader()
        content = header.marshal(response)
        self.conn.sendall(content)

    def on_login(self, header, buf):
        """
        
        :param PacketHeader header: 
        :param BytesIO buf: 
        """
        packet = LoginRequest(buf)
        logging.error('logging password %s', packet.password)
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
        self.conn.sendall(content)

    def on_batch(self, header, buf):
        """
        
        :param PacketHeader header: 
        :param BytesIO buf: 
        :return: 
        """
        cur = time()
        request = SQLBatchRequest(buf)
        self.on_transfer(header, buf)
        logging.error('batch sql elapse %s : %s', time() - cur, request.text)

    def on_transfer(self, header, buf):
        """
        
        :param PacketHeader header: 
        :param BytesIO buf: 
        """
        message = header.marshal(buf)
        db_conn.sendall(message)
        header, buf = self.parse_message_header(db_conn)
        message = header.marshal(buf)
        self.conn.sendall(message)
