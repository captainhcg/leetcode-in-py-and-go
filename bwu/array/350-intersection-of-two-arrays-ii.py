class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1, dict2 = self.numCount(nums1), self.numCount(nums2)
        ret= []
        for key, value in dict1.items():
            if key in dict2:
                ret += [key for _ in xrange(min(value, dict2[key]))]
        return ret
        
    def numCount(self, nums):
        dict = {}
        for n in nums:
            if n not in dict:
                dict[n] = 1
            else:
                dict[n] += 1
        return dict
