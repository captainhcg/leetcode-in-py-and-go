class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
            
        options = set(nums)
        lcs = 0
        
        for i in xrange(len(nums)):
            n = nums[i]
            if n not in options:
                continue
            
            l = 0
            while n in options:
                l += 1
                options.remove(n)
                n += 1
            
            n = nums[i] - 1
            while n in options:
                l += 1
                options.remove(n)
                n -= 1
                
            lcs = max(lcs, l)
            
        return lcs
