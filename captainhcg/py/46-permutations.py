class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.helper(nums)
    
    def helper(self, nums):
        if not nums:
            return [[]]
        ret = []
        for idx, num in enumerate(nums):
            for r in self.helper(nums[:idx] + nums[idx+1:]):
                ret.append([num] + r)
        return ret
