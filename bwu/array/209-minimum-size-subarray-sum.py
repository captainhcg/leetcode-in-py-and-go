class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        left, right = 0, 0
        curr_sum = 0
        min_len = None
        
        while right < len(nums):
            curr_sum += nums[right]
            while curr_sum >= s and left <= right:
                if min_len is None:
                    min_len = right - left + 1
                else:
                    min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1
            right += 1
                
        if min_len is None:
            return 0
        else:
            return min_len
