class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t or abs(len(s) - len(t)) > 1:
            return False
            
        
        if len(s) == len(t):
            diff = 0
            for a, b in zip(s, t):
                if a != b and diff > 0:
                    return False
                elif a != b:
                    diff += 1
        elif len(s) > len(t):
            return self.isOneEditDistance(t, s)
        else:
            for i in xrange(len(s)):
                if s[i] != t[i]:
                    return s[i:] == t[i + 1:]
                    
        return True
