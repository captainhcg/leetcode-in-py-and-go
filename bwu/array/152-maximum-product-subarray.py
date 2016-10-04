class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        ret = nums[0]
        curr_min, curr_max = nums[0], nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] < 0:
                curr_min, curr_max = curr_max, curr_min
            
            curr_max = max(nums[i], nums[i] * curr_max)
            curr_min = min(nums[i], nums[i] * curr_min)
            ret = max(ret, curr_max)
            
        return ret
