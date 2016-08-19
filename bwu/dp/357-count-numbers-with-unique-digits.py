class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 1
            
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 10
        
        factor = 9
        for i in xrange(2, min(11, n + 1)):
            factor *= 11 - i
            dp[i] = dp[i - 1] + factor
        
        return dp[min(n, 10)]
