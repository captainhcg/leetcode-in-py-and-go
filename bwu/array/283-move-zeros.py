class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nz_p = 0
        for i in xrange(len(nums)):
            if nums[i] != 0:
               nums[nz_p] = nums[i]
               nz_p += 1
               
        for i in xrange(nz_p, len(nums)):
            nums[i] = 0
            
        return
