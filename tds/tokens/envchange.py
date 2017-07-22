from cStringIO import StringIO

from tds.utils import b_varchar_encode


class EnvChange(object):
    TOKEN_TYPE = 0xE3
    FMT = "<BH{length}s"

    def __init__(self, params=None):
        """
        
        :param list[tuple(int, str, str)] params: 
        """
        self.buf = StringIO()
        params = params or []
        [self.add_param(*param) for param in params]

    def add(self, env_type, old_value=None, new_value=None):
        """
        
        :param int env_type: 
        :param str old_value: 
        :param str new_value: 
        :return: 
        """
        self.buf.write(chr(env_type))
        self.buf.write(b_varchar_encode(old_value))
        self.buf.write(b_varchar_encode(new_value))

    def __str__(self):
        return ''.join([' {0:02X}'.format(ord(c)) for c in self.marshal()])

    def marshal(self):
        message = self.buf.getvalue()
        length = len(message)
        return ''.join([chr(self.TOKEN_TYPE), chr(length), message])
