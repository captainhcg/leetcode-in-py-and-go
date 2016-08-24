class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return n
            
        idx, curr = 2, 2
        while curr < n:
            if nums[curr] != nums[idx - 2]:
                nums[idx] = nums[curr]
                idx += 1
            
            curr += 1
            
        return idx
