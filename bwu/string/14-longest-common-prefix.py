class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        res = ''
        if n == 0:
            return res
            
        minLen = len(strs[0])
        for s in strs:
            minLen = min(minLen, len(s))

        for i in xrange(minLen):
            ch = strs[0][i]
            for j in xrange(n):
                if strs[j][i] != ch:
                    return res
            res += ch
        return res
