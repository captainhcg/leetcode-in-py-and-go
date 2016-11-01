func min(v1, v2 int64) int64 {
	if v1 < v2 {
		return v1
	}
	return v2
}

func countGap(n, cur1, cur2 int) int {
	ln, lcur1, lcur2 := int64(n), int64(cur1), int64(cur2)
	count := int64(0)
	for lcur1 <= ln {
		count += min(ln+1, lcur2) - lcur1
		lcur1 *= 10
		lcur2 *= 10
	}
	return int(count)
}

func findKthNumber(n int, k int) int {
	k = k - 1
	current := 1
	for k > 0 {
		steps := countGap(n, current, current+1)
		if steps <= k {
			k -= steps
			current++
		} else {
			k--
			current *= 10
		}
	}
	return current
}
