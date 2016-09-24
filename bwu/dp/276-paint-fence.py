class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        res = [0, k, k * k]
        if n < 2:
            return res[n]
            
        for i in xrange(2, n):
            res.append((k - 1) * (res[-1] + res[-2]))
            
        return res[-1]
