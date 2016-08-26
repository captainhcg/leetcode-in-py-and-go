class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        
        ret = []
        cache = {}
        cache[0] = 0
        if not s or not wordDict:
            return ret
            
        n = len(s)
        dp = [True] + [False] * n
        maxLen = max(len(w) for w in wordDict)
        
        for i in xrange(1, n + 1):
            cache[i] = []
            for j in xrange(i):
                if i - j > maxLen:
                    continue
                
                if dp[j] and s[j : i] in wordDict:
                    dp[i] = True
                    if j in cache:
                        cache[i].append(i-j)
                
        ret = []
        arr = []
        
        def dfs(idx):
            if idx == 0:
                ret.append(' '.join(arr[::-1]))
                return
                
            for delta in cache[idx]:
                arr.append(s[idx - delta : idx])
                dfs(idx - delta)
                arr.pop()

        dfs(n)
        return ret
