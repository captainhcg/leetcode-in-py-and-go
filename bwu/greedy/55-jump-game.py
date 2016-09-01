class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        furthest = 0
        for idx, val in enumerate(nums):
            if idx <= furthest and idx + val > furthest:
                furthest = idx + val
                
        return furthest >= len(nums) - 1
