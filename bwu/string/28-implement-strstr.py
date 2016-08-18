class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m, n = len(haystack), len(needle)
        
        if not n:
            return 0
            
        if m < n:
            return -1
            
        for i in xrange(m - n + 1):
            for j in xrange(n):
                if haystack[i + j] != needle[j]:
                    break
                if j == n - 1:
                    return i
        return -1
