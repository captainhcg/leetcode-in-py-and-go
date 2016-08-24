class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(nums)
        if not n:
            return False
            
        l, r = 0, n - 1
        while l + 1 < r:
            mid = (l + r) / 2
            if nums[mid] == target:
                return True
                
            if nums[l] == nums[mid] or nums[l] == nums[r]:
                l += 1
                continue
                
            if nums[mid] > nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid
                else:
                    r = mid
                    
        return nums[l] == target or nums[r] == target
            
