import struct
from cStringIO import StringIO
from collections import OrderedDict
from io import BytesIO

import six
from bunch import Bunch


def data():
    stream = """
12 01 00 2F 00 00 01 00 00 00 1A 00 06 01 00 20 
00 01 02 00 21 00 01 03 00 22 00 04 04 00 26 00 
01 FF 09 00 00 00 00 00 01 00 B8 0D 00 00 01
 """
    stream = stream.split()
    stream = ''.join([chr(int(c, 16)) for c in stream])
    return StringIO(stream)


MAPPING = OrderedDict()
MAPPING[0x00] = ('VERSION', '!LH')
MAPPING[0x01] = ('ENCRYPTION', '!B')
MAPPING[0x02] = ('INSTOPT', None)
MAPPING[0x03] = ('THREADID', '!L')
MAPPING[0x04] = ('MARS', '!B')
MAPPING[0x05] = ('TRACEID', '!16s20s')
MAPPING[0x06] = ('FEDAUTHREQUIRED', '!B')
MAPPING[0x07] = ('NONCEOPT', '!32s')
MAPPING[0xFF] = (None, None)


#
# MAPPING = {
#     0x00: ('VERSION', '!LH'),
#     0x01: ('ENCRYPTION', '!B'),
#     0x02: 'INSTOPT',
#     0x03: ('THREADID', '!L'),
#     0x04: ('MARS', '!B'),
#     0x05: ('TRACEID', '!16s20s'),
#     0x06: ('FEDAUTHREQUIRED', '!B'),
#     0x07: ('NONCEOPT', '!32s'),
#     0xFF: None
# }


def parse_pre_login_packet(buf):
    """
    
    :param BytesIO buf: 
    :return: 
    """
    packet_header = buf.read(8)
    packet_type, status, length, spid, packet, window = struct.unpack("!BBHHBB", packet_header)
    packet_data = buf.read(length)
    entity = dict()
    for i in range(0, len(packet_data), 5):
        token_type, = struct.unpack('!B', packet_data[i])
        if token_type not in MAPPING:
            raise TypeError()

        if token_type == 0xFF:
            # ending token
            break
        position, length = struct.unpack("!HH", packet_data[i + 1: i + 5])
        tmp = packet_data[position: position + length]
        name, fmt = MAPPING.get(token_type)
        if fmt:
            values = struct.unpack(fmt, tmp)
            if len(values) == 1:
                entity[name] = values[0]
            else:
                entity[name] = values
        else:
            entity[name] = tmp

    return Bunch.fromDict(entity)


def marshal_pre_login(params):
    """
    
    :param dict params: 
    :rtype: byte
    """
    options_data = StringIO()
    payload_data = StringIO()
    options = [(key, MAPPING[key]) for key in six.iterkeys(MAPPING) if MAPPING[key][0] in params]
    offset = len(options) + 1

    for key, value in options:

        name, fmt = value
        if fmt:
            name, fmt = value
            length = struct.calcsize(fmt)
            options_data.write(struct.pack('!BHH', key, offset, length))
            payload_data.write(struct.pack(fmt, params.get(name)))
            offset += length
    options_data.write(chr(0xFF))
    options_data.write(payload_data.getvalue())
    return options_data.getvalue()


if __name__ == '__main__':
    print parse_pre_login_packet(buf=data())
    params = Bunch.fromDict(dict(MARS=1, THREADID=3087859712, ENCRYPTION=0))
    stream = marshal_pre_login(params)
    for b in stream:
        print "{0:02X} ".format(ord(b)),
