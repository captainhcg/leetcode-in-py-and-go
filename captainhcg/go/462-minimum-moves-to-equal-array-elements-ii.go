func findK(nums []int, start int, end int, k int) int {
	pivot := nums[end]
	l := start
	for idx := start; idx < end; idx += 1 {
		if nums[idx] < pivot {
			nums[l], nums[idx] = nums[idx], nums[l]
			l += 1
		}
	}
	nums[l], nums[end] = nums[end], nums[l]
	if l == k {
		return pivot
	} else if l < k {
		return findK(nums, l+1, end, k)
	} else {
		return findK(nums, start, l-1, k)
	}
}

func abs(v1, v2 int) int {
	if v1 > v2 {
		return v1 - v2
	}
	return v2 - v1
}

func minMoves2(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	medIdx := len(nums) / 2
	med := findK(nums, 0, len(nums)-1, medIdx)
	cnt := 0
	for _, num := range nums {
		cnt += abs(med, num)
	}
	return cnt
}
