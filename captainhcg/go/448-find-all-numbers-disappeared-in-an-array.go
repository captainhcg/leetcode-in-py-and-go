func findDisappearedNumbers(nums []int) []int {
	ret := make([]int, 0)
	for _, num := range nums {
		idx := num
		if idx < 0 {
			idx = -idx
		}
		if nums[idx-1] > 0 {
			nums[idx-1] = -nums[idx-1]
		}
	}
	for idx, num := range nums {
		if num > 0 {
			ret = append(ret, idx+1)
		}
	}
	return ret
}
