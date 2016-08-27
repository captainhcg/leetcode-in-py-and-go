class NumMatrix(object):
    def __init__(self, matrix):
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if matrix else 0
        self.mat = [[0 for _ in range(self.cols + 1)] for _ in range(self.rows + 1)]
        for y in xrange(self.rows):
            for x in xrange(self.cols):
                self.update(y, x, matrix[y][x])

    def sumRegion(self, row1, col1, row2, col2):
        return self.get(row2, col2) - self.get(row2, col1 - 1) - self.get(row1 - 1, col2) + self.get(row1 - 1, col1 - 1)

    def get(self, y, x):
        cnt = 0
        _y = y + 1
        while _y:
            _x = x + 1
            while _x:
                cnt += self.mat[_y][_x]
                _x -= _x & (-_x)
            _y -= _y & (-_y)
        return cnt

    def update(self, y, x, val):
        _y = y + 1
        while _y <= self.rows:
            _x = x + 1
            while _x <= self.cols:
                self.mat[_y][_x] += val
                _x += _x & (-_x)
            _y += _y & (-_y)
