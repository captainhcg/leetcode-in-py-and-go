class Solution(object):
    def isScramble(self, s1, s2):
        if s1 == s2:
            return True
        elif sorted(s1) != sorted(s2):
            return False

        for idx in xrange(1, len(s1)):
            if self.isScramble(s1[:idx], s2[:idx]) and self.isScramble(s1[idx:], s2[idx:]):
                return True
            if self.isScramble(s1[-idx:], s2[:idx]) and self.isScramble(s1[:-idx], s2[idx:]):
                return True

        return False
