class Solution(object):
    def maxSubArrayLen(self, nums, k):
        if not nums:
            return 0
        arr = [nums[0]]
        for n in nums[1:]:
            arr.append(arr[-1] + n)
        cache = {0: -1}
        maxlen = 0
        for idx, n in enumerate(arr):
            if (n-k) in cache:
                maxlen = max(maxlen, idx-cache[n-k])
            if n not in cache:
                cache[n] = idx
        return maxlen
