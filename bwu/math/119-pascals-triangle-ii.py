class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
                                                                                                                      
        triangle = [[0 for _ in xrange(rowIndex + 1)] for _ in xrange(2)]
        triangle[0][0] = 1
        triangle[1][0] = 1
        triangle[1][1] = 1
    
        for i in xrange(2, rowIndex + 1):
            triangle[i % 2][0] = 1 
            for j in xrange(1, i): 
                triangle[i % 2][j] = triangle[(i - 1) % 2][j - 1] + triangle[(i - 1) % 2][j]
            triangle[i % 2][i] = 1
    
        return triangle[rowIndex % 2]
