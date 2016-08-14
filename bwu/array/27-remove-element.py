class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p, n = 0, len(nums)
        for i in xrange(n):
            if nums[i] != val:
                nums[p] = nums[i]
                p += 1
        return p
