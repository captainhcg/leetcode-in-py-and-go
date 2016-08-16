class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        if n < 1 or k <= 0:
            return False
            
        slow, fast = 0, 0
        seen = set([nums[0]])
        for i in xrange(k):
            fast += 1
            if fast < n and nums[fast] not in seen:
                seen.add(nums[fast])
                continue
            elif fast >= n:
                return False
            else:
                return True
                
        while fast + 1 < n:
            seen.remove(nums[slow])
            slow += 1
            fast += 1
            if nums[fast] in seen:
                return True
            seen.add(nums[fast])
        return False
