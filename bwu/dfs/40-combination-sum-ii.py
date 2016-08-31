class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        self.dfs(sorted(candidates), target, [], ret)
        return ret
        
    def dfs(self, candidates, target, tmp, ret):
        if target == 0:
            ret.append(tmp)
            return
        elif target > 0:
            for i in xrange(len(candidates)):
                if i > 0 and candidates[i] == candidates[i - 1]:
                    continue
                self.dfs(candidates[i+1:], target - candidates[i], tmp + [candidates[i]], ret)
