class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
            
        minP = prices[0]
        maxP = 0
        for p in prices[1:]:
            maxP = max(maxP, p - minP)
            minP = min(minP, p)
        return maxP
