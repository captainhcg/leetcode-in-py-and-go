class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bits = [0] * 32
        n = len(nums)
        for x in nums:
            for i in xrange(32):
                bits[i] += (x & (1 << i)) >> i
            x = x >> 1
        return sum(x * (n - x) for x in bits)
