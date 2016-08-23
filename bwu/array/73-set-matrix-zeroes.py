class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        m, n = len(matrix), len(matrix[0])
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
                    
        for i in rows:
            for j in xrange(n):
                matrix[i][j] = 0
                
        for i in xrange(m):
            for j in cols:
                matrix[i][j] = 0
