class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        global_max = current_max = current_min = nums[0]
        for n in nums[1:]:
            current_max, current_min = max(n, n * current_max, n * current_min), min(n, n * current_max, n * current_min)
            global_max = max(current_max, global_max)
        return global_max
