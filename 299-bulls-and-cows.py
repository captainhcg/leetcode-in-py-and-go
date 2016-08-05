class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        def getBulls():
            cnt = 0
            for a, b in zip(secret, guess):
                if a == b:
                    cnt += 1
            return cnt
        
        def getCows():
            m = collections.defaultdict(int)
            cnt = 0
            for idx, ch in enumerate(secret):
                if secret[idx] == guess[idx]: 
                    continue
                m[ch] += 1
            for idx, ch in enumerate(guess):
                if secret[idx] == guess[idx]: 
                    continue
                if m[ch] > 0:
                    m[ch] -= 1
                    cnt += 1
            return cnt
            
        return "%sA%sB" % (getBulls(), getCows())
