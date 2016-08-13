class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = "".join(ch for ch in s.lower() if ch.isalnum())
        return s == s[::-1]
