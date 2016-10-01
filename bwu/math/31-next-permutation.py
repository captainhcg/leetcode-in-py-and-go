class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        
        p = n - 2
        while p >= 0:
            if nums[p] < nums[p + 1]:
                pivot = self.find(nums, p)
                nums[p], nums[pivot] = nums[pivot], nums[p]
                break
            p -= 1
        self.reverse(nums, p + 1)
        return
    
    def find(self, nums, p):
        for i in xrange(len(nums) - 1, p, -1):
            if nums[i] > nums[p]:
                return i
                
    def reverse(self, nums, p):
        head, tail = p, len(nums) - 1
        while head < tail:
            nums[head], nums[tail] = nums[tail], nums[head]
            head += 1
            tail -= 1
        
