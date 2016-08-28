class Solution(object):
    def findTheDifference(self, s, t):
        import itertools
        c = 0
        for ch in itertools.chain(s, t):
            c ^= ord(ch)
        return chr(c)
