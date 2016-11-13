class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.rows, self.cols = len(matrix), len(matrix[0]) if matrix else 0
        self.bit = [[0 for _ in xrange(self.cols + 1)] for _ in xrange(self.rows + 1)]
        for i in xrange(1, self.rows + 1):
            for j in xrange(1, self.cols + 1):
                self.build(i, j, self.matrix[i - 1][j - 1])
                
    def build(self, x, y, val):
        r, c = [], []
        while x <= self.rows:
            r.append(x)
            x += x & (-x)
        while y <= self.cols:
            c.append(y)
            y += y & (-y)
            
        for i in r:
            for j in c:
                self.bit[i][j] += val

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        self.build(row + 1, col + 1, delta)
        
    def getSum(self, x, y):
        ret = 0
        r, c = [], []
        while x:
            r.append(x)
            x -= x & (-x)
        while y:
            c.append(y)
            y -= y & (-y)
        
        for i in r:
            for j in c:
                ret += self.bit[i][j]
        return ret

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.getSum(row2 + 1, col2 + 1) - self.getSum(row1, col2 + 1) - self.getSum(row2 + 1, col1) + self.getSum(row1, col1)
