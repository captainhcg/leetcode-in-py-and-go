func firstUniqChar(s string) int {
	if len(s) == 0 {
		return -1
	}
	arr := make([]int, 256)
	for idx := range arr {
		arr[idx] = -1
	}
	for idx := 0; idx < len(s); idx += 1 {
		b := s[idx]
		if arr[b] == -1 {
			arr[b] = idx
		} else {
			arr[b] = -2
		}
	}
	min := len(s)
	for _, v := range arr {
		if v >= 0 && v < min {
			min = v
		}
	}
	if min >= 0 && min != len(s) {
		return min
	}
	return -1
}
