class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
            
        n, k = len(costs), len(costs[0])
        dp = [[0 for _ in xrange(k)] for _ in xrange(n)]
        dp[0] = costs[0]
        for i in xrange(1, n):
            for j in xrange(k):
                dp[i][j] = min(dp[i - 1][:j] + dp[i - 1][j + 1:]) + costs[i][j]
                
        return min(dp[n - 1])
