class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1:
            return num2
        if not num2:
            return num1
            
        carry = 0
        res = []
        m, n = len(num1), len(num2)
        for i in xrange(min(m, n)):
            tmp = carry + int(num1[m - 1 - i]) + int(num2[n - 1 - i])
            res.append(str(tmp % 10))
            carry = tmp / 10
            
        if m > n:
            for i in xrange(n, m):
                tmp = carry + int(num1[m - 1 - i])
                res.append(str(tmp % 10))
                carry = tmp / 10
        else:
            for i in xrange(m, n):
                tmp = carry + int(num2[n - 1 - i])
                res.append(str(tmp % 10))
                carry = tmp / 10
                
        if carry:
            res.append('1')
            
        return ''.join(res[::-1])
