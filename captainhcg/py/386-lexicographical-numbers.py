class Solution(object):
    def lexicalOrder(self, n):
        arr = []
        def dfs(start, arr):
            if start <= n:
                arr.append(start)
                start *= 10
                if start <= n:
                    for i in xrange(10):
                        dfs(start + i, arr)

        for i in xrange(1, 10):
            dfs(i, arr)

        return arr
