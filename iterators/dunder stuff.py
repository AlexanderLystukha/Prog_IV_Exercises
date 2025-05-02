class Counter:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __next__(self) -> int:

        if self.current == self.end:
            raise StopIteration("You have reached the end of the counter!")

        self.current += 1

        if (self.current % 2 != 0 and self.current % 3 != 0
                and self.current % 5 != 0 and self.current % 7 != 0):
            return self.current

        if (self.current == 2 or self.current == 3 or self.current == 5
            or self.current == 7):
            return  self.current

    def __iter__(self):
        return self


counter: Counter = Counter(1, 100)
try:
    for i in counter:
        if i is not None:
            print(i)

    a = [1,2,3]
    b = a + [4, 5]

    print(b)

except StopIteration:
    print("cooked")
