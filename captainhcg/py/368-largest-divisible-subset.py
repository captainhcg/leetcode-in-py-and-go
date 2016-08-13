class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        nums.sort()
        dp = [1] * len(nums)
        backtrace = [None] * len(nums)
        maxlen = maxendat= 0
        for idx, divident in enumerate(nums):
            for jdx, divisor in enumerate(nums[:idx]):
                if divident % divisor == 0 and dp[jdx] + 1 > dp[idx]:  # found longer
                    dp[idx] = dp[jdx] + 1
                    backtrace[idx] = jdx
                    if dp[idx] > maxlen:
                        maxlen = dp[idx]
                        maxendat = idx
                        
        # now build output set
        ret = [nums[maxendat]]
        pre_idx = backtrace[maxendat]
        while pre_idx is not None:
            ret.append(nums[pre_idx])
            pre_idx = backtrace[pre_idx]
        
        return ret
