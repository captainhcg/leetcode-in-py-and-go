class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        for n in nums:
            if not dp or n > dp[-1]:
                dp.append(n)
            else:
                to_replace = bisect.bisect_left(dp, n)
                dp[to_replace] = n
        return len(dp)
