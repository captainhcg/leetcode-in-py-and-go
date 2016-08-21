class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if not n:
            return []
        if n == 1:
            return [[1]]
            
        res = [[0 for _ in range(n)] for _ in range(n)]
        val, u, d, l, r = 1, 0, n - 1, 0, n - 1
        while u < d and l < r:
            for i in xrange(l, r):
                res[u][i] = val
                val += 1
            for i in xrange(u, d):
                res[i][r] = val
                val += 1
            for i in xrange(r, l, -1):
                res[d][i] = val
                val += 1
            for i in xrange(d, u, -1):
                res[i][l] = val
                val += 1
            u, d, l, r = u + 1, d - 1, l + 1, r - 1
            
        if l == r:
            res[u][l] = val
        return res
