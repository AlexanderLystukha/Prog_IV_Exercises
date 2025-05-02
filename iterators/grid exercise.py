class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.row = 0
        self.col = 0
        self.current = (self.row, self.col)

    def __iter__(self):
        return self

    def __next__(self):

        if self.row < self.rows:
            self.row += 1

        else:
            self.col += 1
            self.row = 0

        if self.current == (self.rows, self.cols):
            raise StopIteration

        self.current = (self.row, self.col)
        return self.current


grid: Grid = Grid(3, 3)

for i in grid:
    print(i)