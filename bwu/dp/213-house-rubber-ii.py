class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)
        
        v1 = self.helper(nums[:-1])
        v2 = self.helper(nums[1:])
        return max(v1, v2)
        
    def helper(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
            
        dp = [[0 for _ in xrange(2)] for _ in xrange(len(nums))]
        dp[0][0] = nums[0]
        for i in xrange(1, n):
            dp[i][0] = dp[i - 1][1] + nums[i]
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1])
            
        return max(dp[n - 1])
