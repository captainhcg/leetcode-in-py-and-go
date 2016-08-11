class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n1 = n2 = None
        c1 = c2 = 0
        for n in nums:
            if n == n1:
                c1 += 1
            elif n == n2:
                c2 += 1
            elif c1 == 0:
                n1, c1 = n, 1
            elif c2 == 0:
                n2, c2 = n, 1
            else:
                if c1 > 0:
                    c1 -= 1
                if c2 > 0:
                    c2 -= 1
        ret = []
        if c1 > 0 and nums.count(n1) * 3 > len(nums):
            ret.append(n1)
        if c2 > 0 and nums.count(n2) * 3 > len(nums):
            ret.append(n2)
        return ret
