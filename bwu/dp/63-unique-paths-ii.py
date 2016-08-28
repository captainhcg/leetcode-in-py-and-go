class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
            
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in xrange(n)] for _ in xrange(m)]
        
        firstRowObs = False
        for i in xrange(n):
            if obstacleGrid[0][i] == 1:
                firstRowObs = True
            if not firstRowObs:
                dp[0][i] = 1
            else:
                dp[0][i] = 0
                
        firstColObs = False
        for i in xrange(m):
            if obstacleGrid[i][0] == 1:
                firstColObs = True
            if not firstColObs:
                dp[i][0] = 1
            else:
                dp[i][0] = 0
                
        for i in xrange(1, m):
            for j in xrange(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                    
        return dp[m - 1][n - 1]
                
            
