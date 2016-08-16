class Solution(object):
    def coinChange(self, coins, amount):
        arr = [amount+1] * (amount + 1)
        arr[0] = 0
        for coin in coins:
        	for idx in xrange(coin, amount+1):
        		arr[idx] = min(arr[idx-coin]+1, arr[idx])
        return arr[-1] if arr[-1] < amount+1 else -1
