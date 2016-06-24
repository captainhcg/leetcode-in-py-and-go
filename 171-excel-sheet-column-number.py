class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        for idx, ch in enumerate(s[::-1]):
            ret += (ord(ch) - 64) * (26 ** idx)
        return ret
