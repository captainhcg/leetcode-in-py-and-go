class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low + 1 < high:
            mid = (low + high) / 2
            if mid ** 2 == n:
                return mid
            elif mid ** 2 > n:
                high = mid
            else:
                low = mid
                
        if high ** 2 <= n:
            return high
        else:
            return low
