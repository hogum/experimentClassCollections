class ListInstance:

    def __attrnames(self):

        return ' '.join('%s : %s\n' % (attr, self.__dict__[attr])
                        for attr in sorted(self.__dict__))

    def __str__(self):
        return 'Instance of %s(%s)\n\tAddress %s\n\t%s' % (
            self.__class__.__name__,
            self.__supers(),
            id(self),
            self.__attrnames())

    def __supers(self):
        return ', '.join(super_cls.__name__
                         for super_cls in self.__class__.__bases__)
