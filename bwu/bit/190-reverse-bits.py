class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in xrange(32):
            bit = (1 << i) & n
            if bit > 0:
                res ^= 1 << (31 - i)
        return res
