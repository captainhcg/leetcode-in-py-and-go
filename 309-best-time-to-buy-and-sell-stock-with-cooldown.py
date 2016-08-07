class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        buy = [-prices[0], max(-prices[0], -prices[1])]
        sell = [0, max(prices[1]-prices[0], 0)]
        
        for idx in xrange(2, len(prices)):
            buy.append(max(buy[idx-1], sell[idx-2]-prices[idx]))
            sell.append(max(buy[idx-1] + prices[idx], sell[idx-1]))
            
        return sell[-1]
