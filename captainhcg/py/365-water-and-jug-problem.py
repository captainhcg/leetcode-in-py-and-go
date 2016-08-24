class Solution(object):
    def canMeasureWater(self, x, y, z):
        if z == 0:
            return True
        elif x + y < z:
            return False

        def gcd(a, b):
            if a < b:
                return gcd(b, a)
            if not b:
                return a
            return gcd(b, a%b)

        return z % gcd(x, y) == 0
