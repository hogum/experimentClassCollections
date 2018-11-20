
class Mylist:

    def __init__(self, start=[]):
        self.data = list(start)

    def __add__(self, addend):
        return Mylist(self.data + addend)

    def __mul__(self, other):
        return Mylist(self.data * other)

    def __repr__(self):
        return f'{self.data}'

    def __len__(self):
        return len(self.data)

    def __getitem__(self, offset):
        return self.data[offset]

    def __getslice__(self, start, stop):
        return self.data[start, stop]

    def __getattr__(self, attr):
        return getattr(self.data, attr)

    def append(self, other):
        return self.data.append(other)


class MyListSub(Mylist):
    class_calls = 0

    def __init__(self, start):
        self.adds = 0
        Mylist.__init__(self, start)

    def __add__(self, addend):
        print("This is called adding")
        MyListSub.class_calls += 1
        self.adds += 1
        return Mylist.__add__(self, addend)

    def showCount(self):
        return self.adds, self.class_calls
