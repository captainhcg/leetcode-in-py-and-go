class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.ret = []
        self.helper([], nums, len(nums))
        return self.ret

    def helper(self, arr, nums, target):
        for idx in xrange(len(nums)):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            arr.append(nums[idx])
            if len(arr) == target:
                self.ret.append(list(arr))
            else:
                self.helper(arr, nums[:idx] + nums[idx+1:], target)
            arr.pop()
