class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        p1 = p2 = cnt = 0
        while p1 < len(g) and p2 < len(s):
            child = g[p1]
            cookie = s[p2]
            if child <= cookie:
                cnt += 1
                p1 += 1
            p2 += 1
        return cnt
