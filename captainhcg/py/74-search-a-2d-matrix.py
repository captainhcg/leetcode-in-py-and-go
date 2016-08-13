class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        
        def getV(idx):
            row, col = divmod(idx, len(matrix[0]))
            return matrix[row][col]
            
        while left <= right:
            mid = (left + right) / 2
            v = getV(mid)
            if v == target:
                return True
            elif v < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
