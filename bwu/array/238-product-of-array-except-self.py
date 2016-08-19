class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        pl, pr = [1] * n, [1] * n
        
        for i in xrange(1, n):
            pl[i] = pl[i - 1] * nums[i - 1]
            pr[n - 1 - i] = pr[n - i] * nums[n - i]
            
        ret = []
        for a, b in zip(pl, pr):
            ret.append(a * b)
            
        return ret
