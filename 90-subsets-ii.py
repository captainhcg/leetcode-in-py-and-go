class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]
        if not nums:
            return ret
        nums.sort()
        arr = []
        def dfs(idx, lastidx):
            if idx >= len(nums):
                return
            ch = nums[idx]
            dfs(idx+1, lastidx)
            if idx > 0 and ch == nums[idx-1] and lastidx != idx - 1:
                return
            arr.append(ch)
            ret.append(list(arr))
            dfs(idx+1, idx)
            arr.pop()
        dfs(0, -1)
                
        return ret
