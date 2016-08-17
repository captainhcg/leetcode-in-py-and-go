class Solution(object):
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        l = r = total = 0
        minlen = float("inf")
        while r < len(nums):
            total += nums[r]
            if total < s:
                r += 1
                continue
            while l <= r:
                if total >= s:
                    minlen = min(minlen, r - l + 1)
                    total -= nums[l]
                    l += 1
                else:
                    break
            r += 1
        return minlen if minlen != float("inf") else 0
