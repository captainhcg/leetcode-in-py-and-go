class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.ret = []
        self.helper(0, [], candidates, target, -1)
        return self.ret
        
    def helper(self, idx, arr, candidates, remain, last_selected):
        if idx >= len(candidates) or candidates[idx] > remain:
            return
        self.helper(idx+1, arr, candidates, remain, last_selected)
        if idx == 0 or candidates[idx] != candidates[idx-1] or last_selected == idx - 1:
            arr.append(candidates[idx])
            if remain - candidates[idx] == 0:
                self.ret.append(list(arr))
            self.helper(idx+1, arr, candidates, remain - candidates[idx], idx)
            arr.pop()
