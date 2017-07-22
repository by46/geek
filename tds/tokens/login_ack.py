import struct

from tds.utils import b_varchar_encode


class LoginAck(object):
    TOKEN_TYPE = 0xAD
    FMT = '<BHBL{length}s4B'

    def __init__(self):
        self.ack = 0x01
        self.tds_version = 0x01000074
        self.program_name = ""
        self.program_version = (0, 0, 0, 0)

    def marshal(self):
        program_name = b_varchar_encode(self.program_name)
        fmt = self.FMT.format(length=len(program_name))
        length = 10 + len(program_name)
        return struct.pack(fmt, self.TOKEN_TYPE, length, self.ack, self.tds_version,
                           program_name, *self.program_version)
