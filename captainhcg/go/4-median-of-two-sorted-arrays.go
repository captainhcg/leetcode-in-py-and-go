func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
    l := len(nums1) + len(nums2)
    if l % 2 == 0{
        return float64(findKth(nums1, nums2, l/2) + findKth(nums1, nums2, l/2-1)) / 2
    } else {
        return float64(findKth(nums1, nums2, l/2))
    }
}

func findKth(nums1 []int, nums2 []int, kth int) int{
	if len(nums1) >  len(nums2){
		nums1, nums2 = nums2, nums1
	}
	if len(nums1) == 0{
		return nums2[kth]
	}
	if kth == 0{
		return min(nums1[0], nums2[0])
	}
	mid := min(len(nums1) - 1, (kth-1) / 2)
	if kth >= mid{
		if nums1[mid] < nums2[mid]{
			return findKth(nums1[mid+1:], nums2, kth - mid - 1)
		} else {
			return findKth(nums1, nums2[mid+1:], kth - mid - 1)
		}
	} else { // kth < mid
		if nums1[mid] < nums2[mid]{
			return findKth(nums1, nums2[:mid], kth)
		} else {
			return findKth(nums1[:mid], nums2, kth)
		}
	}
}

func min(n1, n2 int) int {
	if n1 > n2{
		return n2
	}
	return n1
}
