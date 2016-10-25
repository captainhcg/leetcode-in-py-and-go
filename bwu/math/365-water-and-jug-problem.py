class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        def gcd(m, n):
            if n > m:
                return gcd(n, m)
            if n == 0:
                return m
            return gcd(n, m % n)
            
        if z == 0:
            return True
        if x + y < z:
            return False
        if x == 0:
            return y == z
        if y == 0:
            return x == z
        tmp = gcd(x, y)
        return z % tmp == 0
