class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n < 2:
            return []
        res = []
        for i in xrange(n - 1):
            if s[i: i + 2] == '++':
                res.append(s[:i] + '--' + s[i + 2:])
        return res
