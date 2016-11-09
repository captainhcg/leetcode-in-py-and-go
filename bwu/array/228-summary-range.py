class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ret = []
        if not nums:
            return ret
        l, r = nums[0], nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] == r + 1:
                r += 1
            else:
                if l == r:
                    ret.append(str(l))
                else:
                    ret.append(str(l) + '->' + str(r))
                l = nums[i]
                r = nums[i]
                
        if l == r:
            ret.append(str(l))
        else:
            ret.append(str(l) + '->' + str(r))
        return ret
            
