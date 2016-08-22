class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        
        while l + 1 < r:
            tmp = (l + r) / 2
            m_x, m_y = tmp / n, tmp % n
            if matrix[m_x][m_y] == target:
                return True
            elif matrix[m_x][m_y] > target:
                r = tmp
            else:
                l = tmp
        
        return matrix[l / n][l % n] == target or matrix[r / n][r % n] == target
