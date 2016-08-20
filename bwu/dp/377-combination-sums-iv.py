class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums, combs = sorted(nums), [0] * (target + 1)
        
        for i in xrange(1, target + 1):
            for n in nums:
                if n > i:
                    break
                elif n == i:
                    combs[i] += 1
                else:
                    combs[i] += combs[i - n]
        return combs[target]
