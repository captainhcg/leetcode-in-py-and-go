class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if n < 2:
            return []
            
        seen = {}
        for i in xrange(n):
            tmp = target - nums[i]
            if tmp in seen:
                return [seen[tmp], i]
            else:
                seen[nums[i]] = i
                
        return []
