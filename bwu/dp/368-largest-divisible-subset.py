class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n < 2:
            return nums
        
        nums.sort()
        dp = [1] * n
        backtrace = [None] * n
        maxLen, maxEndAt = 0, 0
        
        for i, divident in enumerate(nums):
            for j, divisor in enumerate(nums[:i]):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    backtrace[i] = j
                    
                    if dp[i] > maxLen:
                        maxLen = dp[i]
                        maxEndAt = i
                        
        ret = [nums[maxEndAt]]
        while backtrace[maxEndAt] is not None:
            ret.append(nums[backtrace[maxEndAt]])
            maxEndAt = backtrace[maxEndAt]
            
        return ret
