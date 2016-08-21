class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        
        curr_s, min_s = nums[0], min(0, nums[0])
        res = nums[0]
        
        for i in xrange(1, n):
            curr_s += nums[i]
            res = max(res, curr_s - min_s)
            min_s = min(min_s, curr_s)
            
        return res
