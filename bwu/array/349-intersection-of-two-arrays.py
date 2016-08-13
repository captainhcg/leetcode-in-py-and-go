class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1, set2 = set(nums1), set(nums2)
        ret = []
        for n in set1:
            if n in set2:
                ret.append(n)
                
        return ret

        """
        return list(set(nums1) & set(nums2))
        """
