class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
            
        sell, buy = [0] * n, [0] * n
        minP, maxP = prices[0], prices[-1]
        for i in xrange(1, n):
            minP = min(minP, prices[i])
            maxP = max(maxP, prices[n - 1 - i])
            sell[i] = max(sell[i - 1], prices[i] - minP)
            buy[n - 1 - i] = max(buy[n - i], maxP - prices[n - 1 - i])
            
        return max(sell[i] + buy[i] for i in xrange(n))
