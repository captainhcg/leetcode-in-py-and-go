class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and num & (num - 1) == 0 and len("{0:b}".format(num)) % 2 == 1
