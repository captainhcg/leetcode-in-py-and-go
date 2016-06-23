func intersection(nums1 []int, nums2 []int) []int {
	s1 := makeMap(nums1)
	ret := []int{}
	for ele := range makeMap(nums2) {
		if _, present := s1[ele]; present {
			ret = append(ret, ele)
		}
	}
	return ret
}

func makeMap(nums []int) map[int]bool {
	m := map[int]bool{}
	for _, n := range nums {
		m[n] = true
	}
	return m
}
