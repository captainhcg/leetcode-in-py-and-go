class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        res = ''
        
        if num <= 0:
            return res
            
        digit = 0
        while num > 0:
            times = num / nums[digit]
            num -= nums[digit] * times
            res += symbols[digit] * times
            digit += 1
        return res
