class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        if not n:
            return -1
        
        delta = [gas[i] - cost[i] for i in xrange(n)]
        start = 0
        step = 1
        while start < n:
            if delta[start % n] < 0:
                start += 1
                continue
            total = delta[start % n]
            while step < n and total >= 0:
                total += delta[(start + step) % n]
                step += 1
            if step == n and total >= 0:
                return start
            else:
                start = start + step
                step = 0
        return -1
        
