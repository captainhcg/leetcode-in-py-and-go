class Solution(object):
    def wordBreak(self, s, wordDict):
        if not wordDict:
            return []
        back_track = collections.defaultdict(list)
        back_track[-1].append(-1)
        maxlen = max(len(w) for w in wordDict)
        for idx in xrange(len(s)):
            for jdx in xrange(1, maxlen + 1):
                if idx - jdx >= -1 and (idx - jdx) in back_track:
                    if s[idx - jdx + 1:idx + 1] in wordDict:
                        back_track[idx].append(idx - jdx)
        ret = []
        arr = []

        def dfs(idx):
            if idx == -1:
                ret.append(" ".join(arr[::-1]))
                return
            for preIdx in back_track[idx]:
                arr.append(s[preIdx + 1: idx + 1])
                dfs(preIdx)
                arr.pop()

        dfs(len(s) - 1)
        return ret
