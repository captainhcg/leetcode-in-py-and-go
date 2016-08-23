class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [[1 for _ in xrange(2)] for _ in xrange(n)]
        
        if n < 2:
            return n
        for i in xrange(1, n):
            if nums[i] > nums[i - 1]:
                dp[i][0] = max(dp[i - 1][1] + 1, dp[i - 1][0])
            elif nums[i] < nums[i - 1]:
                dp[i][1] = max(dp[i - 1][0] + 1, dp[i - 1][1])
            else:
                dp[i][0] = dp[i - 1][0]
                dp[i][1] = dp[i - 1][1]
                
        return max(dp[n-1])
