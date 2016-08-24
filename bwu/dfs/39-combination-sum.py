class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(candidates, target, [], res)
        return res
        
    def dfs(self, candidates, target, tmp, res):
        if target == 0:
            res.append(tmp)
            return
        if target < 0:
            return
        
        for i in xrange(len(candidates)):
            self.dfs(candidates[i:], target - candidates[i], tmp + [candidates[i]], res)
