class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False for _ in xrange(n + 1)] for _ in xrange(m + 1)]
        dp[0][0] = True
        
        s = " " + s
        p = " " + p
        for i in xrange(1, n + 1):
            if p[i] == '*':
                dp[0][i] = dp[0][i - 2]
            
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if s[i] == p[j] or p[j] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j] == '*':
                    if s[i] != p[j - 1] and p[j - 1] != '.':
                        dp[i][j] = dp[i][j - 2]
                    else:
                        dp[i][j] = dp[i][j - 1] or dp[i - 1][j] or dp[i][j - 2]
                        
        return dp[m][n]
