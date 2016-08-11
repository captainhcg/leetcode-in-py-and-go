class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.ret = []
        self.helper([], 0, candidates, target)
        return self.ret
    
    def helper(self, arr, idx, candidates, target):
        if idx >= len(candidates) or candidates[idx] > target:
            return
        v = candidates[idx]
        self.helper(arr, idx+1, candidates, target)  # do not pick
        if target >= v:
            if target - v == 0:
                self.ret.append(arr + [v])
            else:
                arr.append(v)
                self.helper(arr, idx, candidates, target - v)
                arr.pop()
