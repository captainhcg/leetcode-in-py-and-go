class NumMatrix(object):
    def __init__(self, matrix):
        self.m = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows else 0

        self.bit = []
        for y in range(self.rows + 1):
            self.bit.append([0] * (self.cols + 1))

        for y in range(self.rows):
            for x in range(self.cols):
                v, self.m[y][x] = self.m[y][x], 0
                self.update(y, x, v)

    def update(self, row, col, val):
        diff = val - self.m[row][col]
        y = row + 1
        while y <= self.rows:
            x = col + 1
            while x <= self.cols:
                self.bit[y][x] += diff
                x += x & (-x)
            y += y & (-y)
        self.m[row][col] = val

    def sum(self, row, col):
        y = row + 1
        _sum = 0
        while y > 0:
            x = col + 1
            while x > 0:
                _sum += self.bit[y][x]
                x -= x & (-x)
            y -= y & (-y)
        return _sum

    def sumRegion(self, row1, col1, row2, col2):
        return self.sum(row2, col2) + self.sum(row1-1, col1-1) - self.sum(row2, col1-1) - self.sum(row1-1, col2)
