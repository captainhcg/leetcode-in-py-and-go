class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = 0
        for x, y in zip(secret, guess):
            if x == y:
                bull += 1
        
        cow = sum(min(secret.count(i), guess.count(i)) for i in '0123456789') - bull
        return '%sA%sB' % (bull, cow)
