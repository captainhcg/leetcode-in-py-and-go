class Solution(object):
    def isSubsequence(self, s, t):
        if len(s) > len(t):
            return False
        sidx = tidx = 0
        while sidx < len(s) and tidx < len(t):
            if s[sidx] == t[tidx]:
                sidx += 1
                tidx += 1
            else:
                tidx += 1
        return sidx == len(s)
