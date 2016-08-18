class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a_xor_b = 0
        res1, res2 = 0, 0
        for n in nums:
            a_xor_b ^= n
            
        mask = 1
        for _ in xrange(32):
            mask = mask << 1
            if a_xor_b & mask > 0:
                break
            
        grp1, grp2 = [], []
        for n in nums:
            if n & mask > 0:
                grp1.append(n)
            else:
                grp2.append(n)
                
        for n in grp1:
            res1 ^= n
        for n in grp2:
            res2 ^= n
            
        return [res1, res2]
