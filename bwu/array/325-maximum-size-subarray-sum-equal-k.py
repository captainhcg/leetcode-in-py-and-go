class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = [0] * (len(nums) + 1)
        seen = {}
        seen[0] = -1
        res = 0
        
        for idx, n in enumerate(nums):
            sums[idx + 1] = sums[idx] + n
            if sums[idx + 1] - k in seen:
                res = max(res, idx - seen[sums[idx + 1] - k])
            if sums[idx + 1] not in seen:
                seen[sums[idx + 1]] = idx

        return res
