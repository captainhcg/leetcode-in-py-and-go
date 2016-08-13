class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        chmap = {}
        pmap = {}
        plist = str.split()
        if len(pattern) != len(plist):
            return False
        for s, p in zip(pattern, plist):
            if s in chmap and p in pmap and chmap[s] == p and pmap[p] == s:
                continue
            if s not in chmap and p not in pmap:
                chmap[s] = p
                pmap[p] = s
                continue
            return False
        return True
