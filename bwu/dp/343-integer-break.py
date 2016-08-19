class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        
        dp = [1] * (n + 1)
        for i in xrange(3, n + 1):
            for j in xrange(1, i):
                dp[i] = max(dp[i], max(j, dp[j]) * max((i -j), dp[i - j]))
                
        return dp[n]
