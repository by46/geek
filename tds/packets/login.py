import struct
from io import BytesIO

from tds.utils import decode
from tds.utils import decrypt
from .base import Packet


class LoginPacket(Packet):
    __FIELDS__ = ['client_name', 'username', 'password', 'app_name', 'server_name',
                  'unknown1', 'lib_name', 'locale', 'database']

    def __init__(self):
        self.packet_length = None
        self.tds_version = None
        self.packet_size = None
        self.client_version = None
        self.client_pid = None
        self.connection_id = None
        self.option_flags1 = None
        self.option_flags2 = None
        self.sql_type_flags = None
        self.reserved_flags = None
        self.time_zone = None
        self.collation = None

    def unmarshal(self, buf):
        """

        :param BytesIO buf: 
        """
        params = struct.unpack('<LLLLLLBBBBLL', buf.read(36))
        self.packet_length = params[0]
        self.tds_version = params[1]
        self.packet_size = params[2]
        self.client_version = params[3]
        self.client_pid = params[4]
        self.connection_id = params[5]
        self.option_flags1 = params[6]
        self.option_flags2 = params[7]
        self.sql_type_flags = params[8]
        self.reserved_flags = params[9]
        self.time_zone = params[10]
        self.collation = params[11]

        for field_name in self.__FIELDS__:
            offset, length = struct.unpack('<HH', buf.read(4))
            if not length:
                continue
            old_position = buf.tell()
            buf.seek(offset)
            value = buf.read(length * 2)
            object.__setattr__(self, field_name, decode(value))
            buf.seek(old_position)

        self.password = decrypt(self.password)
