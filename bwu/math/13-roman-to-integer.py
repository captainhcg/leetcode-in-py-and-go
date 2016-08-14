class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ROMAN = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        if s is None or s == '':
            return 0
            
        if len(s) == 1:
            return ROMAN[s[0]]
            
        res = ROMAN[s[-1]]
        for i in xrange(len(s) - 2, -1, -1):
            if ROMAN[s[i]] >= ROMAN[s[i + 1]]:
                res += ROMAN[s[i]]
            else:
                res -= ROMAN[s[i]]
                
        return res
