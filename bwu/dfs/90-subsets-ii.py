class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]
        if not nums:
            return ret
            
        nums.sort()
        
        self.dfs(nums, [], ret)
        return ret
        
    def dfs(self, nums, curr, ret):
        if not nums:
            return
        
        prev = None
        for i in xrange(len(nums)):
            if nums[i] != prev:
                prev = nums[i]
                ret.append(curr + [nums[i]])
                self.dfs(nums[i + 1:], curr + [nums[i]], ret)
