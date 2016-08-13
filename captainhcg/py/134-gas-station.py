class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) - sum(cost) < 0:
            return -1
        profit = 0
        start = 0
        for idx, (g, c) in enumerate(zip(gas, cost)):
            if g - c + profit < 0:
                start = idx + 1
                profit = 0
            else:
                profit = g - c + profit
        return start
