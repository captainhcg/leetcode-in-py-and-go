class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 or not num2:
            return '0'
            
        a, b = len(num1), len(num2)
        res = [0] * (a + b)
        for i in xrange(b - 1, -1, -1):
            for j in xrange(a - 1, -1, -1):
                tmp = (ord(num2[i]) - ord('0')) * (ord(num1[j]) - ord('0'))
                res[i + j + 1] += tmp % 10
                res[i + j] += tmp / 10
                if res[i + j + 1] >= 10:
                    res[i + j + 1] %= 10
                    res[i + j] += 1
                if res[i + j] >= 10 and i + j > 0:
                    res[i + j] %= 10
                    res[i + j - 1] += 1
            
        idx = 0
        while idx < len(res):
            if res[idx] == 0:
                idx += 1
                continue
            return ''.join(map(str,res[idx:]))
        return '0'
