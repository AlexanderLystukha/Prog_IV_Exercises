from typing import Iterable, Iterator


class Enumerate:
    def __init__(self, obj: Iterable):
        self.obj = obj
        self.counter: int = 0

    def __iter__(self):
        self.iterable = iter(self.obj)
        self.counter = 0
        return self

    def __next__(self):
        t = (self.counter, next(self.iterable))
        self.counter += 1
        return t


class Zip:
    def __init__(self, o1, o2, longest: bool, default=None):
        self.o1 = o1
        self.o2 = o2
        self.long = longest
        self.default = default

    def __iter__(self):
        self.iter1 = iter(self.o1)
        self.iter2 = iter(self.o2)

        return self

    def __next__(self):

        first = None
        second = None

        try:
            first = next(self.iter1)
        except StopIteration:
            if self.long:
                first = self.default
        try:
            second = next(self.iter2)
        except StopIteration:
            if self.long:
                second = self.default

        if not self.long and (first is None or second is None):
            raise StopIteration

        if first is None and second is None:
            raise StopIteration

        t = (first, second)

        return t


# hi: Enumerate = Enumerate(["brandon", "is", "very", "AWESOME", "and", "COOL"])
#
# for i in hi:
#     print(i)

a = [(1,2), (3,4)]
b = dict(a)

bye: Zip = Zip(a, b, True)

for i in bye:
    print(i)
