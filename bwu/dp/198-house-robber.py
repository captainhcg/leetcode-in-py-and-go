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
            
        dp = [[0, 0] for _ in xrange(n)]
        dp[0][0] = nums[0]
        
        for i in xrange(1, n):
            dp[i][0] = dp[i - 1][1] + nums[i]
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1])
            
        return max(dp[n - 1][0], dp[n - 1][1])
