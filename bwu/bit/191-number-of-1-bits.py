class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        weight = 0
        while n:
            weight += n & 1
            n = n >> 1
        return weight
