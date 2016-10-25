class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        n = len(nums)
        for i in xrange(n):
            if nums[i] < 1 or nums[i] >= n:
                nums[i] = 0
                
        for i in xrange(n):
            nums[nums[i] % n] += n
            
        for i in xrange(1, n):
            if nums[i] / n == 0:
                return i
        
        return n
