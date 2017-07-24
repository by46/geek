import struct
from cStringIO import StringIO

from tds.base import StreamSerializer
from tds.utils import b_varbyte_encode
from tds.utils import b_varchar_encode


class EnvChange(StreamSerializer):
    TOKEN_TYPE = 0xE3
    FMT = "<BH{length}s"
    ENV_LANGUAGE = 0x02
    ENV_DATABASE = 0x04
    ENV_SQL_COLLATION = 0x07

    def __init__(self, params=None):
        """
        
        :param list[tuple(int, str, str)] params: 
        """
        self.buf = StringIO()
        params = params or []
        [self.add_param(*param) for param in params]

    def add(self, env_type, new_value=None, old_value=None, encode=None):
        """
        
        :param int env_type: 
        :param str old_value: 
        :param str new_value: 
        :param func encode: 
        :return: 
        """
        self.buf.write(chr(env_type))
        encode = encode or b_varchar_encode
        self.buf.write(encode(new_value))
        self.buf.write(encode(old_value))

    def add_bytes(self, env_type, new_value=None, old_value=None):
        self.add(env_type, new_value, old_value, encode=b_varbyte_encode)

    def marshal(self):
        message = self.buf.getvalue()
        length = len(message)
        return ''.join([chr(self.TOKEN_TYPE), struct.pack('<H', length), message])
