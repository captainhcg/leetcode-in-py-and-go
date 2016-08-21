class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n is None or not n:
            return [0]
            
        n1 = [0, 1]
        if n == 1:
            return n1
            
        for i in xrange(1, n):
            n1 = self.step(n1, i)
            
        return n1
        
    def step(self, nums, level):
        nums += reversed(nums)
        
        for i in range(len(nums) / 2, len(nums)):
            nums[i] ^= 1 << level
            
        return nums
