class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l, r = 1, num
        while l + 1 < r:
            mid = (l + r) / 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                r = mid
            else:
                l = mid
                
        if r ** 2 == num or l ** 2 == num:
            return True
        else:
            return False
