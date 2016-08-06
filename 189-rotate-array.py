class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        def reverse(start, end):
            while start < end:
                nums[start], nums[end-1] = nums[end-1], nums[start]
                start += 1
                end -= 1
            
        reverse(0, len(nums)-k)
        reverse(len(nums)-k, len(nums))
        reverse(0, len(nums))
