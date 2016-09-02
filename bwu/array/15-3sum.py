class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        n = len(nums)
        if n < 3:
            return ret
            
        nums.sort()
        for i in xrange(n - 2):
            if 1 <= i < n - 2 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            l, r = i + 1, n - 1
            while l < r:
                tmp = nums[l] + nums[r]
                if tmp == target:
                    ret.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif tmp > target:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                else:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                        
        return ret
