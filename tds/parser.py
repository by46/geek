from StringIO import StringIO
from io import BytesIO
from socket import socket

from .packets import LoginPacket
from .packets import PacketHeader
from .packets import PreLoginPacket


class Parser(object):
    PACKET_TYPES = {
        0x12: PreLoginPacket,
        0x10: LoginPacket
    }

    def __init__(self, conn):
        """
        
        :param socket conn: 
        """
        self.conn = conn

    def parse(self):
        """
        
        :rtype:
        """
        header, data = self.parse_message_header()
        if header.packet_type in self.PACKET_TYPES:
            packet_class = self.PACKET_TYPES.get(header.packet_type)
            packet = packet_class()
            packet.unmarshal(data)
            return packet

    def parse_message_header(self):
        """
        
        :rtype: (PacketHeader, str)
        """
        header = self.conn.recv(8)
        packet_header = PacketHeader()
        packet_header.unmarshal(header)
        data = self.conn.recv(packet_header.length)
        return packet_header, StringIO(data)
