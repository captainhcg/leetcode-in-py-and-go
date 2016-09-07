func strStr(haystack string, needle string) int {
	if needle == ""{
		return 0
	}
	end := len(haystack) - len(needle) + 1
	start := 0
	for start < end {
		offset := 0
		for offset < len(needle) {
			if start+offset < len(haystack) && needle[offset] == haystack[start+offset] {
				offset += 1
			} else {
				break
			}
			if offset == len(needle) {
				return start
			}
		}
		start += 1
	}
	return -1
}
