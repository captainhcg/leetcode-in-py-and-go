class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        if not nums:
            return ret
            
        self.dfs(sorted(nums), [], ret)
        return ret
        
    def dfs(self, nums, tmp, ret):
        if not nums:
            ret.append(tmp)
            return
        
        for i in xrange(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums[:i] + nums[i+1:], tmp + [nums[i]], ret)
