class Solution(object):
    def minCut(self, s):
        def isP(st, ed, cache):
            if cache[st][ed] is not None:
                return cache[st][ed]
            elif s[st] == s[ed]:
                ret = True if st + 1 >= ed else isP(st + 1, ed - 1, cache)
                cache[st][ed] = ret
                return ret
            else:
                cache[st][ed] = False
                return False

        dp = range(1, len(s) + 1)
        cache = [[None] * len(s) for _ in xrange(len(s))]
        for idx in (xrange(len(s))):
            if isP(0, idx, cache):
                dp[idx] = 1
            else:
                for jdx in xrange(1, idx + 1):
                    if isP(jdx, idx, cache):
                        dp[idx] = min(dp[jdx - 1] + 1, dp[idx])
        return dp[-1] - 1
