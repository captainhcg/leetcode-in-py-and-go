class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_s = {}
        map_t = {}
        for x, y in zip(s, t):
            if x in map_s and map_s[x] == y and y in map_t and map_t[y] == x:
                continue
           
            if x not in map_s and y not in map_t:
                map_s[x] = y
                map_t[y] = x
                continue
            
            return False
        return True
