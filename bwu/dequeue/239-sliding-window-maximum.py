class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ret = []
        if not nums:
            return ret
            
        queue = []
        for i in xrange(len(nums)):
            while queue and queue[0] < i - k + 1:
                queue.pop(0)

            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
                
            queue.append(i)
            
            if i >= k - 1:
                ret.append(nums[queue[0]])
                
        return ret
