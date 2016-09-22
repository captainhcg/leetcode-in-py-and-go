class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
            
        seen = {}
        for idx, c in enumerate(s):
            if c in seen:
                seen[c] = -1
            else:
                seen[c] = idx
                
        for c in s:
            if seen[c] != -1:
                return seen[c]
                
        return -1
        
