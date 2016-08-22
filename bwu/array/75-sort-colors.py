class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None:
            return
        
        p_r, p_b = 0, len(nums) - 1
        curr = 0
        while curr <= p_b:
            if nums[curr] == 0:
                nums[curr], nums[p_r] = nums[p_r], nums[curr]
                p_r += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p_b] = nums[p_b], nums[curr]
                p_b -= 1
            else:
                curr += 1
