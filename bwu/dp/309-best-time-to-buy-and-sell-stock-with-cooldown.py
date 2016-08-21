class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
            
        dp = [[0 for _ in xrange(3)] for _ in xrange(n)]
        for i in xrange(1, n):
            dp[i][0] = dp[i - 1][2]
            dp[i][1] = max(dp[i - 1][0] + prices[i] - prices[i - 1], dp[i - 1][1] + prices[i] - prices[i - 1], dp[i - 1][2])
            dp[i][2] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
        return max(dp[n - 1][1], dp[n - 1][2])
