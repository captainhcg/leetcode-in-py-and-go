class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 1]
        for i in xrange(2, n + 1):
            dp[i % 2] = sum(dp)
            
        return dp[n % 2]
