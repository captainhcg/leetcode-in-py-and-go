class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        dp = [False] * len(s)
        for idx in xrange(len(s)):
            for jdx in xrange(idx+1):
                w = s[idx-jdx: idx+1]
                if w in wordDict and (idx == jdx or dp[idx-jdx-1]):
                    dp[idx] = True
                    break
        return dp[-1] if dp else True
