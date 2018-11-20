class Attrs:

    def __init__(self, start):
        self.wrapped = start

    def __getattr__(self, attr):
        return getattr(self.wrapped, attr)

    def __setattr__(self, attr, value):
        print("set", attr, value)
        self.__dict__[attr] = value
