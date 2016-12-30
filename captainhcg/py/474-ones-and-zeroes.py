class Solution(object):
    def findMaxForm(self, strs, m, n):
        def getCount(s):
            n0 = s.count("0")
            return n0, len(s) - n0
            
        mat = [[0] * (n + 1) for _ in xrange(m+1)]
        for s in strs:
            n0, n1 = getCount(s)
            for y in xrange(m, n0-1, -1):
                for x in xrange(n, n1-1, -1):
                    mat[y][x] = max(mat[y][x], mat[y-n0][x-n1] + 1)
        return mat[m][n]
