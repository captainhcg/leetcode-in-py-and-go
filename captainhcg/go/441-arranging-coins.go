func arrangeCoins(n int) int {
	left, right := 1, n>>1+2
	for left < right {
		mid := (left + right) >> 1
		product := (mid * (mid + 1)) >> 1
		if product == n {
			return mid
		} else if product < n {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return right - 1
}
