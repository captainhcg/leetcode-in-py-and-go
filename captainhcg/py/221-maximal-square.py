class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        global_max = 0
        nrow, ncol = len(matrix), len(matrix[0])
        m = [[0] * (ncol + 1) for _ in xrange(nrow + 1)]
        for row in xrange(nrow):
            for col in xrange(ncol):
                if matrix[row][col] == "0":
                    m[row+1][col+1] = 0
                else:
                    v = min(m[row+1][col], m[row][col+1], m[row][col]) + 1
                    m[row+1][col+1] = v
                    global_max = max(global_max, v)
        return global_max ** 2
