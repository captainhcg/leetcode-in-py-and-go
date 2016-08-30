class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return 0
        ret = float('inf')
        
        nums.sort()
        for i in xrange(n - 2):
            new_t = target - nums[i]
            l, r = i + 1, n - 1
            while l < r:
                if nums[l] + nums[r] == new_t:
                    return target
                    
                tmp = nums[l] + nums[r] + nums[i]
                if abs(tmp - target) < abs(ret - target):
                    ret = tmp
                    
                if nums[l] + nums[r] < new_t:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                else:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                        
        return ret
