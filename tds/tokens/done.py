import struct


class Done(object):
    TOKEN_TYPE = 0xFD
    FMT = '<BHHL'

    def __init__(self, status=0, current_cmd=0, done_row_count=0):
        self.status = status
        self.current_cmd = current_cmd
        self.done_row_count = done_row_count

    def marshal(self):
        return struct.pack(self.FMT, self.TOKEN_TYPE, self.status, self.current_cmd, self.done_row_count)
