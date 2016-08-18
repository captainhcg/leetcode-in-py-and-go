class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m, n = len(a), len(b)
        if n < m:
            return self.addBinary(b, a)
        
        carry = 0
        res = ''
        for i in xrange(m):
            tmp = int(a[m - 1 - i]) + int(b[n - 1 - i]) + carry
            res += str(tmp % 2)
            carry = tmp / 2
            print carry
            
        for i in xrange(n - m - 1, -1, -1):
            tmp = int(b[i]) + carry
            res += str(tmp % 2)
            carry = tmp / 2
        
        if carry:
            res += '1'
            
        return res[::-1]
