class Solution(object):
    def threeSumSmaller(self, nums, target):
        count = 0
        nums.sort()
        def ct(start):
            _count = 0
            _sum = nums[start]
            l, r = start + 1, len(nums) - 1
            while l < r:
                if _sum + nums[l] + nums[r] >= target:
                    r -= 1
                else:
                    _count += r - l
                    l += 1
            return _count

        for i in xrange(len(nums) - 2):
            count += ct(i)
        return count
