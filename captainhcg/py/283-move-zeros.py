class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_p = nonzero_p = 0
        length = len(nums)
        while nonzero_p < length:
            if nums[nonzero_p] == 0:
                nonzero_p += 1
                continue
            nums[nonzero_p], nums[zero_p] = nums[zero_p], nums[nonzero_p]
            zero_p += 1
            nonzero_p += 1
