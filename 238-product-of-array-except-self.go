class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return nums
        res = [1] * len(nums)
        for idx in xrange(1, len(nums)):
            res[idx] = res[idx-1] * nums[idx-1]
        
        product = 1
        for idx in xrange(len(nums) - 1, 0, -1):
            product = product * nums[idx]
            res[idx-1] = res[idx-1] * product
        
        return res
