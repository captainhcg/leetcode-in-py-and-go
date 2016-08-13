class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        base = 0
        for idx in xrange(32):
            if n & (1 << idx):
                base |= (1 << 31-idx)
        return base
