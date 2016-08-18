class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        ret = [0] * (num + 1)
        for i in xrange(num + 1):
            ret[i] = ret[i >> 1] + int(i&1)
        return ret
