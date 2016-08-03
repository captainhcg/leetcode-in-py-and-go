import "strconv"

func numDecodings(s string) int {
	ls := len(s)
	if ls == 0 {
		return 0
	} else if ls == 1 {
		if isValid(s) {
			return 1
		} else {
			return 0
		}
	}
	nums := make([]int, len(s))
	if isValid(s[0:1]) {
		nums[0] = 1
	}
	if isValid(s[1:2]) {
		nums[1] = nums[0]
	}
	if isValid(s[0:2]) {
		nums[1] += 1
	}
	for idx := 2; idx < len(s); idx += 1 {
		ways := 0
		if isValid(s[idx: idx+1]) {
			ways += nums[idx-1]
		}
		if isValid(s[idx-1 : idx+1]) {
			ways += nums[idx-2]
		}
		nums[idx] = ways
	}

	return nums[len(s)-1]
}

func isValid(s string) bool {
	if len(s) == 2 && s[0] == '0' {
		return false
	}
	num, _ := strconv.Atoi(s)
	return num > 0 && num <= 26
}
