import struct


class PacketHeader(object):
    FMT = "!BBHHBB"
    TYPE_BATCH = 1
    TYPE_PRE_TDS7 = 2
    TYPE_RPC = 3
    TYPE_RESPONSE = 4
    TYPE_ATTENTION = 6
    TYPE_BULK = 7
    TYPE_REDERATED = 8
    TYPE_LOGIN = 16
    TYPE_PRE_LOGIN = 18

    def __init__(self):
        self.packet_type = None
        self.status = 1
        self.length = None
        self.pid = 1
        self.packet_id = 1
        self.window = 0

    def unmarshal(self, content):
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

    def marshal(self):
        return str(self)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return struct.pack(self.FMT, self.packet_type, self.status, self.length,
                           self.pid, self.packet_id, self.window)
