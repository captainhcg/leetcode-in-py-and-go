class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in xrange(n)] for _ in xrange(m)]
        
        for i in xrange(n):
            dp[0][i] = 1
        for i in xrange(m):
            dp[i][0] = 1
            
        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                
        return dp[m - 1][n - 1]
