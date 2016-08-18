class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        res = [1] * n
        res[0] = res[1] = 0
        for i in xrange(2, n):
            if res[i] == 1:
                for j in xrange(2, (n-1)/i+1):
                    res[i*j] = 0
        return sum(res)
