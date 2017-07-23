import struct
from StringIO import StringIO
from io import BytesIO

import six

from .base import Packet


class PreLoginPacket(Packet):
    __FIELDS__ = ['version', 'encryption', 'inst_opt', 'thread_id', 'mars', 'trace_id', 'fedauth_required', 'nonce_opt']
    OPTIONS = {
        0x00: ('version', '!LH'),
        0x01: ('encryption', '!B'),
        0x02: ('inst_opt', None),
        0x03: ('thread_id', '!L'),
        0x04: ('mars', '!B'),
        0x05: ('trace_id', '!16s20s'),
        0x06: ('fedauth_required', '!B'),
        0x07: ('nonce_opt', '!32s'),
        0xFF: None
    }
    TERMINATOR = 0xFF

    def __init__(self):
        pass

    def unmarshal(self, buf):
        """

        :param BytesIO buf: 
        :return: 
        """
        while True:
            token_type, = struct.unpack('!B', buf.read(1))
            if token_type not in self.OPTIONS:
                raise ValueError()
            if token_type == self.TERMINATOR:
                break
            position, length = struct.unpack("!HH", buf.read(4))
            old_position = buf.tell()
            buf.seek(position)
            tmp = buf.read(length)
            name, fmt = self.OPTIONS.get(token_type)
            if fmt:
                values = struct.unpack(fmt, tmp)
                setattr(self, name, values[0] if len(values) == 1 else values)
            else:
                setattr(self, name, tmp)
            buf.seek(old_position)

    def marshal(self):
        """
        construct stream packet
        :rtype: str 
        """
        options_data = StringIO()
        payload_data = StringIO()
        options = []
        for key in sorted(six.iterkeys(self.OPTIONS)):
            if key == self.TERMINATOR:
                continue
            name, fmt = self.OPTIONS.get(key)
            if getattr(self, name, None):
                options.append((key, name, fmt))

        offset = len(options) * 5 + 1

        for key, name, fmt in options:
            if fmt:
                length = struct.calcsize(fmt)
                options_data.write(struct.pack('!BHH', key, offset, length))
                params = getattr(self, name)
                if not isinstance(params, tuple):
                    params = (params,)
                payload_data.write(struct.pack(fmt, *params))
                offset += length
            else:
                options_data.write(struct.pack('!BHH', key, offset, 1))
                payload_data.write(getattr(self, name))
                offset += 1

        options_data.write(chr(0xFF))
        options_data.write(payload_data.getvalue())
        return options_data.getvalue()
