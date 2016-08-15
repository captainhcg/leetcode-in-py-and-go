func trap(height []int) int {
	left, right := 0, len(height) - 1
	blocks, stones := 0, 0
	left_height, right_height := 0, 0
	for left <= right {
		if height[left] > left_height {
			left_height = height[left]
		}
		if height[right] > right_height {
			right_height = height[right]
		}
		if left_height <= right_height {
			blocks += left_height
			stones += height[left]
			left += 1
		} else {
			blocks += right_height
			stones += height[right]
			right -= 1
		}
	}
	return blocks - stones
}
