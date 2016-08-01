func divide(dividend int, divisor int) int {
	MAX_INT := 2147483647
	if divisor == 0 {
		return MAX_INT
	}

	dividend64, divisor64 := int64(dividend), int64(divisor)
	neg := false
	if (dividend64 < 0 && divisor64 > 0) || (dividend64 > 0 && divisor64 < 0) {
		neg = true
	}
	if dividend64 < 0 {
		dividend64 = -dividend64
	}
	if divisor64 < 0 {
		divisor64 = -divisor64
	}
	ret := 0
	move_left := uint(0)
	for divisor64 < dividend64 && (divisor64<<move_left) < dividend64 {
		move_left += 1
	}
	for {
		if dividend64 >= (divisor64 << move_left) {
			ret += (1 << move_left)
			dividend64 -= (divisor64 << move_left)
		}
		if move_left == 0 {
			break
		} else {
			move_left -= 1
		}
	}
	if neg {
		ret = -ret
	}
	if ret > MAX_INT {
		return MAX_INT
	}
	return ret
}
