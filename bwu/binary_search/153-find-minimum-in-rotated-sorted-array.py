class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l, r = 0, n - 1
        while l + 1 < r:
            mid = (l + r) / 2
            if nums[r] < nums[l]:
                if nums[mid] > nums[l]:
                    l = mid
                else:
                    r = mid
            else:
                return nums[l]
                
        return min(nums[l], nums[r])
