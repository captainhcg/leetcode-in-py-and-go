class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.l = nums
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        index, count, nums = -1, 0, self.l
        for i in xrange(len(nums)):
            if nums[i] == target:
                if random.randint(0,count) == 0:
                    index = i
                count += 1
        return index
