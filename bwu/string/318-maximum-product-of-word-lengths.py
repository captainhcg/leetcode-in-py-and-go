class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        mapping = {}
        for word in words:
            mask = self.getMask(word)
            l = len(word)
            if mask not in mapping:
                mapping[mask] = l
            elif l > mapping[mask]:
                mapping[mask] = l
                
        res = 0
        for k1, v1 in mapping.iteritems():
            for k2, v2 in mapping.iteritems():
               if k1 & k2 > 0:
                   continue
               res = max(res, v1 * v2)
               
        return res
        
    def getMask(self, word):
        base = 0
        for c in word:
            base |= 1 << (ord(c) - ord('a'))
        return base
