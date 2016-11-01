class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        self.kSum(sorted(nums), 4, target, [], results)
        return results
        
    def kSum(self, nums, N, target, result, results):
        if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:
            return
        
        if N == 2:
            left, right = 0, len(nums) - 1
            while left < right:
                tmp = nums[left] + nums[right]
                if tmp == target:
                    results.append(result + [nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif tmp > target:
                    right -= 1
                else:
                    left += 1
        else:
            for i in xrange(len(nums) - N + 1):
                if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                    self.kSum(nums[i + 1:], N - 1, target - nums[i], result + [nums[i]], results)
