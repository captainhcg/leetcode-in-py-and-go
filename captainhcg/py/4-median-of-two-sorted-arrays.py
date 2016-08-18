class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        def find_k(arr1, arr2, kth):
            if len(arr1) > len(arr2):
                arr2, arr1 = arr1, arr2
            if not arr1:
                return arr2[kth]
            if kth == 0:
                return min(arr1[0], arr2[0])
            m = min(len(arr1)-1, (kth-1)/2)
            if kth > m:
                if arr1[m] >= arr2[m]:
                    return find_k(arr1, arr2[m+1:], kth - m - 1)
                else:
                    return find_k(arr1[m+1:], arr2, kth - m - 1)
            else:  # kth <= m
                if arr1[m] >= arr2[m]:
                    return find_k(arr1[:m], arr2, kth)
                else:
                    return find_k(arr1, arr2[:m], kth)

        lensum = len(nums1) + len(nums2)
        if lensum % 2 == 1:
            m = find_k(nums1, nums2, lensum >> 1)
            return float(m)
        else:
            l = find_k(nums1, nums2, lensum >> 1)
            r = find_k(nums1, nums2, (lensum >> 1) - 1)
            return float(l + r) / 2
