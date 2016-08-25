func search(nums []int, target int) bool {
	left, right := 0, len(nums)-1
	for left <= right {
		md := (left + right) / 2
		mdv := nums[md]
		if mdv == target {
			return true
		}
		if mdv > nums[left] {
			if target < mdv && nums[left] <= target {
				right = md - 1
			} else {
				left = md + 1
			}
		} else if mdv < nums[left] {
			if target > mdv && nums[right] >= target {
				left = md + 1
			} else {
				right = md - 1
			}
		} else {
			left += 1
		}
	}
	return false
}
