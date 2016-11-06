class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return -1
        if dividend == 0:
            return 0
            
        MAX_INT = 2 ** 31 - 1
        MIN_INT = - 2 ** 31
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        sign = -1   
        if divisor > 0 and dividend > 0 or divisor < 0 and dividend < 0:
            sign = 1
        
        dd = abs(dividend)
        ds = abs(divisor)
        res = 0
        queue = []
        
        while ds <= dd:
            queue.append(ds)
            ds += ds
            
        for i in xrange(len(queue) - 1, -1, -1):
            if dd >= queue[i]:
                dd -= queue[i]
                res += 2 ** i
        return res * sign
