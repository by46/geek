from cStringIO import StringIO


class Response(object):
    def marshal(self):
        """
        
        :rtype: str 
        """


class LoginResponse(Response):
    def __init__(self):
        self.components = []
        self.buf = StringIO()

    def add_component(self, component):
        self.components.append(component)

    def marshal(self):
        self.buf.truncate()
        [self.buf.write(component.marshal()) for component in self.components]
        return self.buf.getvalue()
