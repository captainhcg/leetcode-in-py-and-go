class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        cols = set()
        rows = set()
        for idx in xrange(len(matrix)):
            for jdx in xrange(len(matrix[0])):
                if matrix[idx][jdx] == 0:
                    cols.add(jdx)
                    rows.add(idx)
        for idx in rows:
            for jdx in xrange(len(matrix[0])):
                matrix[idx][jdx] = 0
        for jdx in cols:
            for row in matrix:
                row[jdx] = 0
