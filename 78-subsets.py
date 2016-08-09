class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        self.ret = []
        self.helper([], 0, nums)
        return self.ret
        
    def helper(self, arr, idx, nums):
        if idx == len(nums) - 1:
            self.ret.append(list(arr))
            self.ret.append(arr + [nums[idx]])
        else:
            self.helper(arr, idx+1, nums)
            arr.append(nums[idx])
            self.helper(arr, idx+1, nums)
            arr.pop()
