class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(n, k, 1, [], res)
        return res
        
    def dfs(self, n, k, start, tmp, res):
        if k == 0:
            res.append(tmp)
            return
        
        for i in xrange(start, n + 1):
            self.dfs(n, k - 1, i + 1, tmp + [i], res)
