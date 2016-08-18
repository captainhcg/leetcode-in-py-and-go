class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, n - k, n - 1)
        self.reverse(nums, 0, n - 1)
        return
        
        
    def reverse(self, nums, head, tail):
        while head < tail:
            nums[head], nums[tail] = nums[tail], nums[head]
            head += 1
            tail -= 1
        return
