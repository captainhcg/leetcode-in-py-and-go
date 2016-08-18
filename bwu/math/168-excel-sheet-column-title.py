class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        while n:
            res += chars[(n - 1) % 26]
            n = (n - 1) / 26
        return res[::-1]
