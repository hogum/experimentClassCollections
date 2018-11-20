class Set:

    def __init__(self, start):
        self.wrapped = []
        self.make_set(start)

    def intersect(self, other):
        res = [item for item in other if item in self.wrapped]
        return Set(res)

    def union(self, other):
        res = self.wrapped[:]
        for item in other:
            if item not in res:
                res.append(item)

        return Set(res)

    def make_set(self, values):
        for value in values:
            if value not in self.wrapped:
                self.wrapped.append(value)

    def __len__(self):
        return len(self.wrapped)

    def __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return 'Set' + repr(self.wrapped)

    def __iter__(self):
        return iter(self.wrapped)


class ArbitrarySet(Set):

    def intersect(self, *others):
        res = []
        for item in others:
            for x in item:
                if x not in self:
                    break
                res.append(x)
        return Set(res)

    def union(self, *others):
        res = []
        for item in others:
            for x in item:
                if x not in res:
                    res.append(x)

        return Set(res)
