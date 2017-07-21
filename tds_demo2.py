from io import BytesIO

from tds.packets import PreLoginPacket
from tds.utils import beautify_hex

if __name__ == '__main__':
    packet = PreLoginPacket()
    packet.inst_opt = '\x00'
    packet.version = (123456, 1)
    packet.encryption = 2
    packet.thread_id = None
    content = packet.marshal()
    beautify_hex(content)
    buf = BytesIO(content)
    new_packet = PreLoginPacket()
    new_packet.unmarshal(buf)

    print
