import struct

from tds.base import StreamSerializer
from tds.utils import b_varchar_encode


class Login7Stream(StreamSerializer):
    def __init__(self):
        pass


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
