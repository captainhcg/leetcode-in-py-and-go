class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or len(matrix) == 1:
            return
            
        m, n = len(matrix), len(matrix[0])
        for i in range(m / 2):
            for j in range((n + 1) / 2):
                matrix[i][j], matrix[j][m - 1 - i], matrix[m - 1 - i][n - 1 - j], matrix[n - 1 - j][i] = matrix[n - 1 - j][i], matrix[i][j], matrix[j][m - 1 - i], matrix[m - 1 - i][n - 1 - j]
        
        return
