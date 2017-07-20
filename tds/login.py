import struct
from io import BytesIO


def parse_login_packet(buf):
    """
    
    :param BytesIO buf: 
    :return: 
    """
    packet_header = buf.read(8)
    packet_type, status, length, spid, packet, window = struct.unpack("!BBHHBB", packet_header)
    print struct.unpack('<L', buf.read(4))
    print '{0:X}'.format(*struct.unpack('<L', buf.read(4)))
    print struct.unpack('<L', buf.read(4))
    print struct.unpack('<L', buf.read(4))
    print struct.unpack('<L', buf.read(4))
    print struct.unpack('<L', buf.read(4))

    # 4 Flags
    print '{0:02X} {1:02X} {2:02X} {3:02X}'.format(*struct.unpack('<BBBB', buf.read(4)))
    # Time Zone
    print '{0:02X}'.format(*struct.unpack('<L', buf.read(4)))
    # Collation
    print '{0:02X}'.format(*struct.unpack('<L', buf.read(4)))
    print '{0} - {1}'.format(*struct.unpack('<HH', buf.read(4)))
    print '{0} - {1}'.format(*struct.unpack('<HH', buf.read(4)))
    print '{0} - {1}'.format(*struct.unpack('<HH', buf.read(4)))


if __name__ == '__main__':
    print parse_login_packet(mock())
