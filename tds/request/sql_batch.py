from io import RawIOBase

from tds.tokens import SQLBatchStream


class SQLBatchRequest(object):
    def __init__(self, buf):
        """

        :param RawIOBase buf: 
        """
        self.stream = stream = SQLBatchStream()
        stream.unmarshal(buf)

    def __getattr__(self, item):
        return getattr(self.stream, item)
