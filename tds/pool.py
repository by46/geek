import logging
from StringIO import StringIO
from socket import socket

from tds.packets import PacketHeader
from tds.tokens import Login7Stream
from tds.tokens import PreLoginStream
from tds.utils import beautify_hex


def main():
    conn = socket()
    conn.connect(('10.1.25.24', 1433))

    # pre-login
    stream = PreLoginStream()
    stream.version = (1426128904, 0)
    stream.encryption = PreLoginStream.ENCRYPT_NOT_SUP
    stream.inst_opt = "EHISSQL"
    stream.thread_id = 9999
    packet = PacketHeader()
    packet.packet_type = PacketHeader.TYPE_PRE_LOGIN
    beautify_hex(stream.marshal())
    conn.sendall(packet.marshal(stream))

    header = conn.recv(8)
    packet.unmarshal(header)
    data = conn.recv(packet.length)
    buf = StringIO(data)
    stream.unmarshal(buf)

    # login

    stream = Login7Stream()
    stream.client_version = 4176642822
    stream.client_pid = 14228
    stream.connection_id = 0
    stream.option_flags1 = 0xf0
    stream.option_flags2 = 0x01
    stream.sql_type_flags = 0x00
    stream.reserved_flags = 0x00
    stream.time_zone = 0xFFFFFF88
    stream.collation = 0x00000436
    stream.client_name = 'WCMIS035'
    stream.username = "CTIDbo"
    stream.password = "Dev@CTIdb0"
    stream.app_name = "pymssql=2.1.3"
    stream.server_name = "S1DSQL04\\EHISSQL"
    stream.lib_name = "DB-Library"
    stream.locale = 'us_english'
    stream.database = 'CTI'

    packet = PacketHeader()
    packet.packet_type = PacketHeader.TYPE_LOGIN
    beautify_hex(stream.marshal())
    # conn.sendall(packet.marshal(stream))

    message = "\x10\x01\x00\xf6\x00\x00\x00\x00\xee\x00\x00\x00\x01\x00\x00\x71\x00\x10\x00\x00\x06\x83\xf2\xf8\x80\x28\x00\x00\x00\x00\x00\x00\xf0\x01\x00\x00\x88\xff\xff\xff\x36\x04\x00\x00\x56\x00\x08\x00\x66\x00\x06\x00\x72\x00\x0a\x00\x86\x00\x0d\x00\xa0\x00\x10\x00\x00\x00\x00\x00\xc0\x00\x0a\x00\xd4\x00\x0a\x00\xe8\x00\x03\x00\x00\x00\x00\x00\x00\x00\xee\x00\x00\x00\xee\x00\x00\x00\x57\x00\x43\x00\x4d\x00\x49\x00\x53\x00\x30\x00\x33\x00\x35\x00\x43\x00\x54\x00\x49\x00\x44\x00\x62\x00\x6f\x00\xe1\xa5\xf3\xa5\xc2\xa5\xa1\xa5\x91\xa5\xe0\xa5\x31\xa5\xe3\xa5\x83\xa5\xa6\xa5\x70\x00\x79\x00\x6d\x00\x73\x00\x73\x00\x71\x00\x6c\x00\x3d\x00\x32\x00\x2e\x00\x31\x00\x2e\x00\x33\x00\x53\x00\x31\x00\x44\x00\x53\x00\x51\x00\x4c\x00\x30\x00\x34\x00\x5c\x00\x45\x00\x48\x00\x49\x00\x53\x00\x53\x00\x51\x00\x4c\x00\x44\x00\x42\x00\x2d\x00\x4c\x00\x69\x00\x62\x00\x72\x00\x61\x00\x72\x00\x79\x00\x75\x00\x73\x00\x5f\x00\x65\x00\x6e\x00\x67\x00\x6c\x00\x69\x00\x73\x00\x68\x00\x43\x00\x54\x00\x49\x00"
    conn.sendall(message)
    header = conn.recv(8)
    packet.unmarshal(header)
    data = conn.recv(packet.length)
    buf = StringIO(data)
    stream.unmarshal(buf)
    logging.error(stream.username)
    conn.close()


if __name__ == '__main__':
    main()
