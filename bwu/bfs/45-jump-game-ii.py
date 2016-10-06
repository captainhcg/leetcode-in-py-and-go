class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 1:
            return 0
            
        start, end, currMax = 0, nums[0], 0
        level = 1
        
        while end < len(nums) - 1:
            next_end = end
            level += 1
            for i in xrange(start, end + 1):
                next_end = max(next_end, i + nums[i])
            start += 1
            end = next_end
        return level
