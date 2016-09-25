class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def find_kth(A, B, k):
            if len(A) > len(B):
                return find_kth(B, A, k)
            if len(A) == 0:
                return B[k-1]
                
            if k == 1:
                return min(A[0], B[0])
                
            a = A[k / 2 - 1] if len(A) >= k / 2 else None
            b = B[k / 2 - 1] if len(B) >= k / 2 else None
            
            if b is None or a < b and a is not None:
                return find_kth(A[k / 2:], B, k - k / 2)
            else:
                return find_kth(A, B[k / 2:], k - k / 2)
                
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return find_kth(nums1, nums2, l//2 + 1)
        else:
            return (find_kth(nums1, nums2, l//2 + 1) + find_kth(nums1, nums2, l//2)) / 2.0
        
