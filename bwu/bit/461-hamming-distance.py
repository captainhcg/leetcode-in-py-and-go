class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = 0
        tmp = x ^ y
        while tmp:
            res += 1
            tmp &= (tmp - 1)
        return res
