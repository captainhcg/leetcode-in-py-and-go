class Solution(object):
    def isMatch(self, s, p):
        self.cache = set()
        return self.helper(s[::-1] + "#", 0, p[::-1] + "#", 0)

    def helper(self, s, l, p, r):
        if (l, r) in self.cache:
            return False

        while l < len(s) and r < len(p):
            if s[l] == p[r] or p[r] == ".":
                l += 1
                r += 1
            elif p[r] == "*":
                if s[l] == p[r + 1] or p[r + 1] == ".":
                    res = self.helper(s, l + 1, p, r + 2) or\
                        self.helper(s, l + 1, p, r) or\
                        self.helper(s, l, p, r + 2)
                    if res:
                        return True
                    else:
                        self.cache.add((l, r))
                        return False
                else:
                    r += 2
            else:
                self.cache.add((l, r))
                return False
        if l == len(s) and r == len(p):
            return True
        self.cache.add((l, r))
        return False
