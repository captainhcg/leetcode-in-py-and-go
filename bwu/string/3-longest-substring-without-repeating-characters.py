class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
            
        maxL = 0
        currL = 0
        seen = set([])
        start, end = 0, 0
        while end < len(s):
            if s[end] not in seen:
                seen.add(s[end])
                currL += 1
                end += 1
                maxL = max(currL, maxL)
            else:
                while s[start] != s[end]:
                    seen.remove(s[start])
                    currL -= 1
                    start +=1
                    
                seen.remove(s[start])
                currL -= 1
                start +=1
        return maxL
                
