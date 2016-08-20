class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in xrange(32):
            count = 0
            for n in nums:
                count += n >> i & 1
            if i == 31 and count % 3:
                res -= 1 << 31
            else:
                res ^= (count % 3) << i
            
        return res
