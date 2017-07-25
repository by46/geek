from io import RawIOBase

from tds.tokens import PreLoginStream


class PreLoginRequest(object):
    def __init__(self, buf):
        """
        
        :param RawIOBase buf: 
        """
        self.stream = stream = PreLoginStream()
        stream.unmarshal(buf)

    def __getattr__(self, item):
        return getattr(self.stream, item)
