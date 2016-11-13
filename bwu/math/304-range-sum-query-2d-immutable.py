class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.m, self.n = len(matrix), len(matrix[0]) if matrix else 0
        self.sum_matrix = [[0 for _ in xrange(self.n  + 1)] for _ in xrange(self.m + 1)]
        for i in xrange(1, self.m + 1):
            for j in xrange(1, self.n + 1):
                self.sum_matrix[i][j] = self.sum_matrix[i][j - 1] + self.sum_matrix[i - 1][j] - self.sum_matrix[i - 1][j - 1] + matrix[i - 1][j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sum_matrix[row2 + 1][col2 + 1] - self.sum_matrix[row1][col2 + 1] - self.sum_matrix[row2 + 1][col1] + self.sum_matrix[row1][col1]
