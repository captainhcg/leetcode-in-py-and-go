func buildArr(s string) (arr []int) {
	arr = make([]int, len(s))
	for idx := 0; idx < len(s); idx += 1 {
		if idx == 0 {
			arr[idx] = -1
		} else if arr[idx-1] > 0 && s[idx] == s[arr[idx-1]] {
			arr[idx] = arr[idx-1] + 1
		} else if s[idx] == s[0] {
			arr[idx] = 1
		}
	}
	return
}

func reverse(s string) string {
	r := []byte(s)
	i, j := 0, len(s)-1
	for i <= j {
		r[i], r[j] = r[j], r[i]
		i += 1
		j -= 1
	}
	return string(r)
}

func shortestPalindrome(s string) string {
	reversed_s, arr := reverse(s), buildArr(s) // searh for s in reversed_s, thus bulid kmp map for s
	i, offset, suffix, max_len := 0, 0, -1, 0
	for (i+offset) < len(s) && offset < len(s) {
		if reversed_s[i+offset] == s[offset] {
			suffix = arr[offset]
			offset += 1
			if i+offset == len(s) { // early termination
				max_len = offset
				break
			}
		} else {
			i += offset - suffix
			suffix = -1
			offset = 0
		}
	}
	return reverse(s[max_len:len(s)]) + s
}
