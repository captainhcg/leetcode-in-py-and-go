class Solution(object):
    def multiply(self, A, B):
        if not A or not B:
            return []
        mat = [[0] * len(B[0]) for _ in range(len(A))]
        anumidx = []
        bnumidx = []

        for y in xrange(len(A)):
            anumidx.append(set())
            for x in xrange(len(A[0])):
                if A[y][x] != 0:
                    anumidx[-1].add(x)

        for x in xrange(len(B[0])):
            bnumidx.append(set())
            for y in xrange(len(B)):
                if B[y][x] != 0:
                    bnumidx[-1].add(y)

        for y in xrange(len(A)):
            if not anumidx[y]:
                continue
            for x in xrange(len(B[0])):
                if not bnumidx[x]:
                    continue
                mat[y][x] = sum(A[y][n] * B[n][x] for n in anumidx[y] & bnumidx[x])

        return mat
