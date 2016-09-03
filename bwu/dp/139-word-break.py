class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if not wordDict:
            return False
            
        maxLen = max(len(w) for w in wordDict)
        n = len(s)
        dp = [True] + [False] * n
        for end in xrange(1, n + 1):
            for start in xrange(end):
                if dp[start]:
                    if len(s[start: end]) > maxLen:
                        continue
                    if s[start: end] in wordDict:
                        dp[end] = True
                        break
        
        return dp[n]
