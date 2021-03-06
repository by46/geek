import logging
from datetime import datetime
from io import BytesIO
from socket import socket
from time import time

from bunch import Bunch

import user
from pool import manager
from tds import mq
from tds.exceptions import AbortException
from tds.packets import PacketHeader
from tds.request import LoginRequest
from tds.request import PreLoginRequest
from tds.request import SQLBatchRequest
from tds.response import LoginResponse
from tds.tokens import Collation
from tds.tokens import DoneStream
from tds.tokens import EnvChangeStream
from tds.tokens import InfoStream
from tds.tokens import LoginAckStream
from tds.tokens import PreLoginStream
from tds.tokens import parse_tokens

EVENT_LOGIN = "login"
EVENT_LOGOUT = "logout"
EVENT_INPUT = "input"
EVENT_OUTPUT = "output"
EVENT_BATCH = "batch"


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

    def __init__(self, conn, address, logger=None):
        self.logger = logger or logging.getLogger(__name__)
        self.conn = conn
        self.client_ip = address[0]

    def run(self):
        while True:
            try:
                header, data = self.parse_message_header()
                if header.packet_type in self.PROCESS:
                    method = getattr(self, self.PROCESS.get(header.packet_type))
                    method(header, data)
                else:
                    logging.error('Unknown packet: %s', header.packet_type)
                    self.on_transfer(header, data)
            except AbortException as e:
                self.logger.exception(e)
                self._send_logout_event()
                break

    def parse_message_header(self, conn=None):
        """
        :param socket conn:
        :rtype: (PacketHeader, BytesIO)
        """
        conn = conn or self.conn
        header = conn.recv(self.PACKET_HEADER_LENGTH)
        if len(header) < self.PACKET_HEADER_LENGTH:
            # TODO(benjamin): process disconnection
            raise AbortException()
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
        self._send_login_event()

        logging.error('logging password %s', packet.password)
        response = LoginResponse()
        env1 = EnvChangeStream()
        env1.add(1, 'CTI', 'master')
        sql_collation = Collation()
        env2 = EnvChangeStream()
        env2.add_bytes(EnvChangeStream.ENV_SQL_COLLATION, sql_collation.marshal())
        env3 = EnvChangeStream()
        env3.add(EnvChangeStream.ENV_LANGUAGE, 'us_english')
        ack = LoginAckStream()
        ack.program_name = "TDS"
        env = EnvChangeStream()
        env.add(EnvChangeStream.ENV_DATABASE, '4096', '4096')
        done = DoneStream()
        info = InfoStream()
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
        # TODO(benjamin): process batch error
        self._send_batch_event(elapse, request.text, error=None)

    def on_transfer(self, header, buf, parse_token=False):
        """
        
        :param PacketHeader header: 
        :param BytesIO buf: 
        :param bool parse_token: 
        :rtype: [StreamSerializer]
        """
        message = header.marshal(buf)
        pool = manager.get_connection(self.settings)
        with pool.get() as conn:
            conn.sendall(message)
            self._send_input_event(message)
            header, response_buf = self.parse_message_header(conn)
        message = header.marshal(response_buf)
        self.conn.sendall(message)
        self._send_output_event(message)
        items = parse_tokens(response_buf)

    def _make_event(self, event):
        stamp = datetime.now().strftime('%Y%m%d%H%M%S%f')[:-3]

        return Bunch(event=event,
                     user=self.user,
                     database=self.database,
                     client_ip=self.client_ip,
                     stamp=stamp)

    def _send_output_event(self, message):
        event = self._make_event(event=EVENT_OUTPUT)
        event.size = len(message)
        mq.send(event)

    def _send_input_event(self, message):
        event = self._make_event(event=EVENT_INPUT)
        event.size = len(message)
        mq.send(event)

    def _send_batch_event(self, elapse, text, error):
        event = self._make_event(event=EVENT_BATCH)
        event.elapse = elapse
        event.text = text
        event.error = error
        mq.send(event)

    def _send_login_event(self):
        event = self._make_event(event=EVENT_LOGIN)
        mq.send(event)

    def _send_logout_event(self):
        event = self._make_event(event=EVENT_LOGOUT)
        mq.send(event)
