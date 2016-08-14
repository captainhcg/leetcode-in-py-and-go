class Solution(object):
    def generatePossibleNextMoves(self, s):
        ret = []
        for idx in xrange(len(s)):
            if s[idx:idx+2] == "++":
                ret.append(s[:idx] + "--" + s[idx+2:])
        return ret
