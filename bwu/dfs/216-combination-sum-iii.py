class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(k, n, [], 1, res)
        return res
        
    def dfs(self, k, target, tmp, start, res):
        if target < 0:
            return
        
        if k == 0 and target == 0:
            res.append(tmp)
            return
        
        for i in xrange(start, 10):
            self.dfs(k - 1, target - i, tmp + [i], i + 1, res)
