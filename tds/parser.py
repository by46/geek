import struct
from StringIO import StringIO
from io import BytesIO

from .encrypt import decrypt


class PreLoginPacket(object):
    def __init__(self, buff):
        pass


class LoginPacket(object):
    FIELDS = ('client_name', 'username', 'password', 'app_name', 'server_name',
              'unknown1', 'lib_name', 'locale', 'database')

    def __init__(self, buf):
        """
        
        :param BytesIO buf: 
        """
        params = struct.unpack('<LLLLLLBBBBLL', buf.read(36))
        self.packet_length = params[0]
        self.tds_version = params[1]
        self.tds_version = params[2]
        self.client_version = params[3]
        self.client_pid = params[4]
        self.connection_id = params[5]
        self.option_flags1 = params[6]
        self.option_flags2 = params[7]
        self.sql_type_flags = params[8]
        self.reserved_flags = params[9]
        self.time_zone = params[10]
        self.collation = params[11]
        fields = []
        for field_name in self.FIELDS:
            offset, length = struct.unpack('<HH', buf.read(4))
            fields.append((field_name, offset, length))

        for field_name, offset, length in fields:
            if length:
                buf.seek(offset)
                value = buf.read(length * 2)
                value = ''.join([c for c in value if c != '\x00'])
                object.__setattr__(self, field_name, value)

        self.password = decrypt(self.password)


class Parser(object):
    PACKET_TYPES = {
        0x12: PreLoginPacket,
        0x10: LoginPacket
    }

    def __init__(self, conn):
        self.conn = conn  # type: BytesIO

    def parse(self):
        """
        
        :rtype:
        """
        header, data = self.parse_message_header()
        if header.packet_type in self.PACKET_TYPES:
            packet_class = self.PACKET_TYPES.get(header.packet_type)
            packet = packet_class(data)
            print(packet)

    def parse_message_header(self):
        """
        
        :rtype: (PacketHeader, str)
        """
        header = self.conn.read(8)
        packet_header = PacketHeader(header)
        data = self.conn.read(packet_header.length)
        return packet_header, StringIO(data)


class PacketHeader(object):
    FMT = "!BBHHBB"

    def __init__(self, content):
        """
        
        :param str content: 
        """
        packet_type, status, length, pid, packet_id, window = struct.unpack(self.FMT, content)
        self.packet_type = packet_type
        self.status = status
        self.length = length
        self.pid = pid
        self.packet_id = packet_id
        self.window = window

    def __repr__(self):
        return str(self)

    def __str__(self):
        return struct.pack(self.FMT, self.packet_type, self.status, self.length,
                           self.pid, self.packet_id, self.window)


def mock():
    data = """
10 01 00 f6 00 00 00 00 ee 00 00 00 01 00 00 71
00 10 00 00 06 83 f2 f8 e0 23 00 00 00 00 00 00
f0 01 00 00 88 ff ff ff 36 04 00 00 56 00 08 00
66 00 06 00 72 00 0a 00 86 00 0d 00 a0 00 10 00
00 00 00 00 c0 00 0a 00 d4 00 0a 00 e8 00 03 00
00 00 00 00 00 00 ee 00 00 00 ee 00 00 00 57 00
43 00 4d 00 49 00 53 00 30 00 33 00 35 00 43 00
54 00 49 00 44 00 62 00 6f 00 e1 a5 f3 a5 c2 a5
a1 a5 91 a5 e0 a5 31 a5 e3 a5 83 a5 a6 a5 70 00
79 00 6d 00 73 00 73 00 71 00 6c 00 3d 00 32 00
2e 00 31 00 2e 00 33 00 53 00 31 00 44 00 53 00
51 00 4c 00 30 00 34 00 5c 00 45 00 48 00 49 00
53 00 53 00 51 00 4c 00 44 00 42 00 2d 00 4c 00
69 00 62 00 72 00 61 00 72 00 79 00 75 00 73 00
5f 00 65 00 6e 00 67 00 6c 00 69 00 73 00 68 00
43 00 54 00 49 00
"""
    stream = data.split()
    stream = ''.join([chr(int(c, 16)) for c in stream])
    return StringIO(stream)

