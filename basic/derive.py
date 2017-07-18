class IterIO(object):
    def __new__(cls, gen):
        if isinstance(gen, int):
            return IterI(gen)
        return IterO(gen)


class IterI(IterIO):
    def __new__(cls, gen):
        self = object.__new__(cls)
        self._gen = gen
        return self


class IterO(IterIO):
    def __new__(cls, gen):
        self = object.__new__(cls)
        self._gen = gen
        return self


class NumberFactory(object):
    def __new__(cls):
        return bool()


if __name__ == '__main__':
    x = IterIO('benj')
    print x, isinstance(x, IterIO)
    y = NumberFactory()
    print y, isinstance(y, NumberFactory)
