func sortTransformedArray(nums []int, a int, b int, c int) []int {
	ret := make([]int, len(nums))
	var start_idx int
	if a >= 0 {
		start_idx = len(nums) - 1
	} else {
		start_idx = 0
	}
	l, r := 0, len(nums)-1
	for l <= r {
		if helper(nums[l], a, b, c) > helper(nums[r], a, b, c) {
			if a >= 0 {
				ret[start_idx] = helper(nums[l], a, b, c)
				start_idx -= 1
				l += 1
			} else {
				ret[start_idx] = helper(nums[r], a, b, c)
				start_idx += 1
				r -= 1
			}
		} else {
			if a >= 0 {
				ret[start_idx] = helper(nums[r], a, b, c)
				start_idx -= 1
				r -= 1
			} else {
				ret[start_idx] = helper(nums[l], a, b, c)
				start_idx += 1
				l += 1
			}
		}
	}
	return ret
}

func helper(n, a, b, c int) int {
	return n*n*a + b*n + c
}
