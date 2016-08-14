class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        n = len(digits)
        for i in xrange(n - 1, -1, -1):
            tmp = digits[i] + carry
            carry = tmp / 10
            digits[i] = tmp % 10

        if carry:
            return [1] + digits
        else:
            return digits
