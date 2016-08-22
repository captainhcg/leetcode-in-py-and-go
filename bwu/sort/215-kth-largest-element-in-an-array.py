class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.findKthSmallest(nums, 0, len(nums) - 1, len(nums) - k)
        
    def findKthSmallest(self, nums, l, r, target):
        pivot = nums[r]
        idx = l
        for i in xrange(l, r):
            if nums[i] < pivot:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
        nums[idx], nums[r] = nums[r], nums[idx]
        
        if idx == target:
            return nums[idx]
        elif idx > target:
            return self.findKthSmallest(nums, l, idx - 1, target)
        else:
            return self.findKthSmallest(nums, idx + 1, r, target)
