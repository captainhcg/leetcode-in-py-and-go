class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        mapping = {
            '0': '0',
            '1': '1',
            '6': '9',
            '9': '6',
            '8': '8'
            }
            
        n = len(num)
        for i in xrange(n / 2 + 1):
            if num[i] not in mapping or mapping[num[i]] != num[n - 1 - i]:
                return False
        return True
