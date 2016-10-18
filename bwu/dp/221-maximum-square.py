class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        max_len = 0
        if not matrix or not matrix[0]:
            return max_len
            
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in xrange(n)] for _ in xrange(m)]
        
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                elif matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                max_len = max(max_len, dp[i][j])
        
        return max_len ** 2
