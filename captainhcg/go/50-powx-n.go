func myPow(x float64, n int) float64 {
	if x == 0.0 {
		return 0.0
	}
	flap := false
	if n < 0 {
		n = -n
		flap = true
	}
	base := x
	result := 1.0
	for n > 0 {
		if n&1 > 0 {
			result *= base
		}
		n = n >> 1
		base = base * base
	}
	if flap == true {
		result = 1.0 / result
	}
	return result
}
