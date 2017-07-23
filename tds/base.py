from io import BytesIO


class StreamSerializer(object):
    def marshal(self):
        """
        serialize into tds stream bytes stream
        :return: 
        """
        return self.__class__.__name__

    def unmarshal(self, buf):
        """
        unserialize info from tds stream bytes stream
        :param BytesIO buf: 
        """

    def __str__(self):
        return ''.join([' {0:02X}'.format(ord(c)) for c in self.marshal()])

    def __repr__(self):
        return ''.join([' {0:02X}'.format(ord(c)) for c in self.marshal()])
