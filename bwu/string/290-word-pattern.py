class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(' ')
        ms, mt = {}, {}
        if len(words) != len(pattern):
            return False
            
        for a, b in zip(list(pattern), words):
            if a in ms and b in mt and ms[a] == b and mt[b] == a:
                continue
            if a not in ms and b not in mt:
                ms[a] = b
                mt[b] = a
                continue
            return False
            
        return True
