class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p, n = 1, len(nums)
        if n == 0:
            return 0
            
        for i in xrange(1, n):
            if nums[i] != nums[i - 1]:
                nums[p] = nums[i]
                p += 1
        return p
