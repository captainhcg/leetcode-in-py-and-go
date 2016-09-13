class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        cache = {}

        def dfs(y, x):
            if (y, x) not in cache:
                val = matrix[y][x]
                currentlen = 1
                for newy, newx in ((y+1, x), (y-1, x), (y, x+1), (y, x-1)):
                    if newy < 0 or newy >= len(matrix) or newx < 0 or newx >= len(matrix[0]):
                        continue
                    elif matrix[newy][newx] <= val:
                        continue
                    currentlen = max(currentlen, dfs(newy, newx) + 1)
                cache[(y, x)] = currentlen
            return cache[(y, x)]

        maxlen = 1
        for row in xrange(len(matrix)):
            for col in xrange(len(matrix[0])):
                maxlen = max(dfs(row, col), maxlen)

        return maxlen
