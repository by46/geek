from io import BytesIO

from six import add_metaclass


class DefaultFieldsMetaClass(type):
    def __new__(cls, name, bases, attributes):
        if name == 'Packet':
            return type.__new__(cls, name, bases, attributes)
        fields = attributes.get('__FIELDS__', [])
        for name in fields:
            if isinstance(name, tuple):
                name, default_or_type = name
                if type(default_or_type) is type:
                    default_or_type = default_or_type()
            else:
                default_or_type = None
            attributes[name] = default_or_type
        return type.__new__(cls, name, bases, attributes)


@add_metaclass(DefaultFieldsMetaClass)
class Packet(object):
    def marshal(self):
        pass

    def unmarshal(self, buf):
        """
        
        :param BytesIO buf: 
        :return: 
        """
