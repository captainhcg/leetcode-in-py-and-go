class Solution(object):
    def maxProfit(self, k, prices):
        if len(prices) < 2:
            return 0
        if k >= len(prices) / 2:
            return self.helper(prices)
        buy_array = [0] + [float('-inf')] * k
        sell_array = [0] * (k + 1)
        for p in prices:
            for idx in xrange(1, k + 1):
                buy_array[idx] = max(buy_array[idx], -p + sell_array[idx-1])
                sell_array[idx] = max(sell_array[idx], p + buy_array[idx])
        return sell_array[-1]
    
    def helper(self, prices):
        profit = 0
        last_p = prices[0]
        for p in prices[1:]:
            if p > last_p:
                profit += p - last_p
            last_p = p
        return profit
