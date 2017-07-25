import struct
from io import RawIOBase

from tds.base import StreamSerializer
from tds.utils import b_varchar_encode
from tds.utils import decrypt


class Login7Stream(StreamSerializer):
    __FIELDS__ = ['client_name', 'username', 'password', 'app_name', 'server_name',
                  'unknown1', 'lib_name', 'locale', 'database']

    def __init__(self):
        super(Login7Stream, self).__init__()
        self.tds_version = 0x01000074
        self.packet_size = 4096
        self.client_version = 0
        self.client_pid = 0
        self.connection_id = 0
        self.option_flags1 = 0
        self.option_flags2 = 0
        self.sql_type_flags = 0
        self.reserved_flags = 0
        self.time_zone = 0
        self.collation = 0
        self.client_name = None
        self.username = None
        self.password = None
        self.app_name = None
        self.server_name = None
        self.unknown1 = None
        self.lib_name = None
        self.locale = None
        self.database = None

    def unmarshal(self, buf):
        """
        
        :param RawIOBase buf: 
        """
        params = struct.unpack('<LLLLLLBBBBLL', buf.read(36))
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
            if field_name == 'password':
                value = decrypt(value)
            else:
                value = value.decode('utf-16-le')
            object.__setattr__(self, field_name, value)
            buf.seek(old_position)


class LoginAckStream(StreamSerializer):
    TOKEN_TYPE = 0xAD

    def __init__(self):
        self.ack = 0x01
        self.tds_version = 0x01000074
        self.program_name = None
        self.program_version = (0, 0, 0, 0)
        super(LoginAckStream, self).__init__()

    def marshal(self):
        self.buf.truncate()
        self.buf.write(chr(self.ack))
        self.buf.write(struct.pack('<L', self.tds_version))
        self.buf.write(b_varchar_encode(self.program_name))
        self.buf.write(struct.pack('<4B', *self.program_version))
        return super(LoginAckStream, self).marshal()
