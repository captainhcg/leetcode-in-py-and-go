class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        length = len(str)
        i = 0
        sign = 1
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -MAX_INT - 1
        
        if not str:
            return 0
        
        while i < length and str[i] == ' ':
            i += 1
            
        if i < length and str[i] == '+':
            i += 1
        elif i < length and str[i] == '-':
            sign = -1
            i += 1
            
        ret = 0
        while i < length and str[i] >= '0' and str[i] <= '9':
            num = ord(str[i]) - ord('0')
            if ret > MAX_INT / 10 or num > MAX_INT - ret * 10:
                return MIN_INT if sign == -1 else MAX_INT
                
            ret = ret * 10 + num
            i += 1
        
        return sign * ret
