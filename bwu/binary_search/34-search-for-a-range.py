class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if not n:
            return [-1, -1]
            
        left, right = -1, -1
        
        l, r = 0, n - 1
        while l + 1 < r:
            mid = (l + r) / 2
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        if nums[l] == target:
            left = l
        elif nums[r] == target:
            left = r
            
        l, r = 0, n - 1
        while l + 1 < r:
            mid = (l + r) / 2
            if nums[mid] > target:
                r = mid
            else:
                l = mid
        if nums[r] == target:
            right = r
        elif nums[l] == target:
            right = l
            
        return [left, right]
                
