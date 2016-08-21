class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
            
        l, r = 0, n - 1
        while l + 1 < r:
            mid = (l + r) / 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid
            else:
                r = mid
                
        if nums[r] < target:
            return r + 1
        elif nums[l] < target:
            return r
        else:
            return l
