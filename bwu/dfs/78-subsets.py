class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, curr, res):
        if not nums:
            return
        
        for i in xrange(len(nums)):
            res.append(curr + [nums[i]])
            self.dfs(nums[i + 1:], curr + [nums[i]], res)
