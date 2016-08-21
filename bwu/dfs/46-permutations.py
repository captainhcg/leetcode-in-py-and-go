class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, tmp, res):
        if not len(nums):
            res.append(tmp)
            return
        
        for i in xrange(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], tmp + [nums[i]], res)
