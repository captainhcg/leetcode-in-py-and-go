class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret, length = 0, len(s)
        for i in xrange(length):
            ret = ret * 26 + ord(s[i]) - ord('A') + 1
            
        return ret
