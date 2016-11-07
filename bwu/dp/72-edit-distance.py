class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1 and not word2:
            return 0
        m, n = len(word1), len(word2)
        if not word1:
            return n
        if not word2:
            return m
            
        dp = [[0 for _ in xrange(n + 1)] for _ in xrange(m + 1)]
        for i in xrange(n + 1):
            dp[0][i] = i
        for i in xrange(m + 1):
            dp[i][0] = i
            
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j] + 1, dp[i][j - 1] + 1)
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1)
        return dp[m][n]
