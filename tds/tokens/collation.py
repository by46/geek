from tds.base import StreamSerializer


class Collation(StreamSerializer):
    def marshal(self):
        return '\x09\x04\xd0\x00\x34'
