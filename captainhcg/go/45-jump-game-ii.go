func jump(nums []int) int {
	last_jump, this_jump, jumps := 0, 0, 0
	for idx, jump := range nums[:len(nums)-1] {
		this_jump = max(this_jump, idx + jump)
		if idx == last_jump {
			last_jump = this_jump
			jumps += 1
		}
	}
	return jumps
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
