class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = []
        while n > 26:
            n, idx = divmod(n-1, 26)
            ret.append(chr(65 + idx))
        ret.append(chr(65 + n -1))
        return "".join(ret[::-1])
