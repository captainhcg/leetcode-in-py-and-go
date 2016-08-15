class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        p, res = x, 0
        while p:
            res = res * 10 + p % 10
            p /= 10
        return res == x
