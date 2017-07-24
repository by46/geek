import struct
from cStringIO import StringIO
from io import BytesIO


class StreamSerializer(object):
    TOKEN_TYPE = 0x00

    def __init__(self):
        # self.buf = StringIO()
        pass

    def marshal(self):
        """
        serialize into tds stream bytes stream
        :return: 
        """
        message = self.buf.getvalue()
        length = len(message)
        return ''.join([chr(self.TOKEN_TYPE), struct.pack('<H', length), message])

    def unmarshal(self, buf):
        """
        unserialize info from tds stream bytes stream
        :param BytesIO buf: 
        """

    def __str__(self):
        return ''.join([' {0:02X}'.format(ord(c)) for c in self.marshal()])

    def __repr__(self):
        return ''.join([' {0:02X}'.format(ord(c)) for c in self.marshal()])
