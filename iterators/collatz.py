import timer


class Collatz:

    def __init__(self, start):
        self.start: int = start
        self.current: int = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == 1:
            raise StopIteration

        if self.current % 2 == 0:
            self.current = self.current // 2
        if self.current % 2 == 1:
            self.current = 3 * self.current + 1

        return self.current

hi = Collatz(6921)

for i in hi:
    print(i)





