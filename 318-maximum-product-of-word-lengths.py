class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d = {}
        for w in words:
            mask = self.getMask(w)
            l = len(w)
            if mask not in d:
                d[mask] = l
            elif l > d[mask]:
                d[mask] = l
        
        maxm = 0
        for k1, v1 in d.iteritems():
            for k2, v2 in d.iteritems():
                if k1 & k2:
                    continue
                maxm = max(maxm, v1 * v2)
        
        return maxm
    
    def getMask(self, word):
        base = 0
        for ch in word:
            base |= 1 << (ord(ch) - 97)
        return base
