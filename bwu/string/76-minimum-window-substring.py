class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ''
            
        mapping = {}
        for c in t:
            if c not in mapping:
                mapping[c] = 1
            else:
                mapping[c] += 1
                
        counter = len(t)
        ret = ''
        b = 0
        
        while b < len(s):
            if s[b] in mapping:
                break
            b += 1
            
        e = b
        while e < len(s):
            if s[e] in mapping:
                if mapping[s[e]] > 0:
                    counter -= 1
                mapping[s[e]] -= 1
                
            while counter == 0:
                if ret == '' or e - b + 1 < len(ret):
                    ret = s[b: e + 1]
                
                if s[b] in mapping:
                    mapping[s[b]] += 1
                    if mapping[s[b]] > 0:
                        counter += 1
                b += 1
            e += 1
                    
        return ret
