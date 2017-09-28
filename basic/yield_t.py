class Demo(object):
    @property
    def names(self):
        for i in range(10):
            yield i

if __name__ == '__main__':
    demo = Demo()
    for name in demo.names:
        print(name)