class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n
        digits = 1
        pos = 0
        step = 1
        while pos + digits * (10 ** digits - step) < n:
            pos += digits * (10 ** digits - step)
            digits += 1
            step *= 10
        delta = n - pos - 1
        d = delta % digits
        n = delta / digits
        start = 10 ** (digits - 1)
        target = start + n
        return int(str(target)[d])
