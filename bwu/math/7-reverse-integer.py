class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        
        neg = False
        if x < 0:
            neg = True
            x = -x
        
        res = 0
        while x:
            res = res * 10 + x % 10
            x /= 10
            
        if res > (2 ** 31 - 1):
            return 0
            
        if neg:
            return -res
        else:
            return res
