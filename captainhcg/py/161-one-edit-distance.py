class Solution(object):
    def isOneEditDistance(self, s, t):
        if s == t or abs(len(s) - len(t)) > 1:
            return False
        pre, post = 0, 0
        for c1, c2 in zip(s, t):
            if c1 == c2:
                pre += 1
            else:
                break
        if post + pre == max(len(s), len(t)) - 1:
            return True
        for c1, c2 in zip(s[::-1], t[::-1]):
            if c1 == c2:
                post += 1
            else:
                break
        return post + pre == max(len(s), len(t)) - 1
