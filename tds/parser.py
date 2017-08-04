import logging
from datetime import datetime
from io import BytesIO
from socket import socket
from time import time

from bunch import Bunch

import user
from pool import manager
from tds import mq
from tds.packets import PacketHeader
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


class Parser(object):
    """
    :type conn: socket
    """
    PROCESS = {
        0x01: 'on_batch',
        0x10: 'on_login',
        0x12: 'on_pre_login'
    }
    PACKET_HEADER_LENGTH = 8
    conn = None
    user = None
    client_ip = None
    database = None
    db_conn = None
    settings = {}

    def __init__(self, conn, address):
        self.conn = conn
        self.client_ip = address[0]

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
        header = conn.recv(self.PACKET_HEADER_LENGTH)
        if len(header) < self.PACKET_HEADER_LENGTH:
            # TODO(benjamin): process disconnection
            raise Exception()
        packet_header = PacketHeader()
        packet_header.unmarshal(header)
        length = packet_header.length - self.PACKET_HEADER_LENGTH
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
        info = user.login(packet.username, packet.password)
        if info is None:
            # TODO(benjamin): process login failed
            pass
        self.settings = {
            "user": "CTIDbo",
            "password": "Dev@CTIdb0",
            "instance": "S1DSQL04\\EHISSQL",
            "database": "CTI",
            "ip": "S1DSQL04",
            "port": 1433
        }
        self.user = packet.username
        self.database = packet.database
        event = self._make_event(event='login')
        mq.send(event)

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
        elapse = time() - cur
        logging.error('batch sql elapse %s : %s', time() - cur, request.text)
        # TODO(benjamin): process error
        event = self._make_event(event='batch')
        event.elapse = elapse
        event.text = request.text
        event.error = None
        mq.send(event)

    def on_transfer(self, header, buf):
        """
        
        :param PacketHeader header: 
        :param BytesIO buf: 
        """
        event = self._make_event('input')
        event.size = len(buf.getvalue())
        mq.send(event)
        message = header.marshal(buf)
        pool = manager.get_connection(self.settings)
        with pool.get() as conn:
            conn.sendall(message)
            header, buf = self.parse_message_header(conn)
        message = header.marshal(buf)
        self.conn.sendall(message)

    def _make_event(self, event):
        stamp = datetime.now().strftime('%Y%m%d%H%M%S')

        return Bunch(event=event,
                     user=self.user,
                     database=self.database,
                     client_ip=self.client_ip,
                     stamp=stamp)
