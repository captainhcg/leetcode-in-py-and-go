class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_p = 0
        n = len(prices)
        if n < 2:
            return max_p
        
        p = 0
        for curr in xrange(1, n):
            if prices[curr] < prices[curr - 1]:
                max_p += prices[curr - 1] - prices[p]
                p = curr
        
        max_p += prices[-1] - prices[p]
        return max_p
