from collections import Counter

class Solution(object):
    def canPermutePalindrome(self, s):
        c = Counter(s)
        odds = 0
        for ch, cnt in c.iteritems():
            odds += cnt & 1
            if odds > 1:
                return False
        return True
