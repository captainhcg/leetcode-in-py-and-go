class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        n = len(prices)
        if n < 2 or k < 1:
            return 0
            
        min_p = 0
        if k > n / 2:
            for i in xrange(1, n):
                if prices[i] > prices[i - 1]:
                    total += prices[i] -prices[i - 1]
            return total
        else:
            dp = [[0 for _ in xrange(n)] for _ in xrange(k + 1)]
            for i in xrange(1, k + 1):
                local = dp[i - 1][0] - prices[0]
                for j in xrange(1, n):
                    dp[i][j] = max(dp[i][j - 1], local + prices[j])
                    local = max(local, dp[i - 1][j] - prices[j])
            return dp[k][n - 1]
