class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: iint
        :rtype: int
        """
        return self.findK(nums, 0, len(nums)-1, len(nums) - k)
    
    def findK(self, nums, lo, hi, kidx):
        storeIdx, pivot = lo, nums[hi]
        for idx in xrange(storeIdx, hi):
            if nums[idx] < pivot:
                nums[storeIdx], nums[idx] = nums[idx], nums[storeIdx]
                storeIdx += 1
        nums[storeIdx], nums[hi] = nums[hi], nums[storeIdx]
        if storeIdx == kidx:
            return nums[storeIdx]
        elif storeIdx < kidx:
            return self.findK(nums, storeIdx+1, hi, kidx)
        else:
            return self.findK(nums, lo, storeIdx-1, kidx)
