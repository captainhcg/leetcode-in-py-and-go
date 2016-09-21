class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length < 2:
            return s
            
        start, maxLen, idx = 0, 0, 0

        while idx < length:
            left, right = idx, idx
            while right + 1 < length and s[right + 1] == s[left]:
                idx += 1
                right += 1
                
            while left - 1 >= 0 and right + 1 < length and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1
                
            if right - left + 1 > maxLen:
                maxLen = right - left + 1
                start = left
            
            idx += 1
            
        return s[start: start + maxLen]
