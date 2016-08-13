func min(l, r int) int {
    if l < r{
        return l
    } else {
        return r
    }
}

func maxArea(height []int) int {
    if len(height) < 2{
        return 0
    }
    left, right := 0, len(height) - 1
    max_area := min(height[left], height[right]) * (right - left)
    for left < right {
        area := min(height[left], height[right]) * (right - left)
        if area > max_area {
            max_area = area
        }
        if height[left] > height[right] {
            right -= 1
        } else {
            left += 1
        }
    }
    return max_area
}
