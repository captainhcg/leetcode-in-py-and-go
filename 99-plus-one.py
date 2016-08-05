class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ret = []
        add = 1
        for idx in xrange(len(digits)-1, -1, -1):
            add, val = divmod(digits[idx] + add, 10)
            ret.append(val)
        if add:
            ret.append(1)
        return ret[::-1]
