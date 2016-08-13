class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sm = {}
        tm = {}
        for l, r in zip(s, t):
            if l in sm and r in tm and sm[l] == r and tm[r] == l:
                continue
            elif l not in sm and r not in tm:
                sm[l] = r
                tm[r] = l
                continue
            return False
        return True
