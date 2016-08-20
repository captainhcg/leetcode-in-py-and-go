class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
            
        if n == 2:
            return 2
            
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2
        
        for i in xrange(3, n + 1):
            for j in xrange(i):
                dp[i] += dp[j] * dp[i - 1 - j]
                
        return dp[n]
