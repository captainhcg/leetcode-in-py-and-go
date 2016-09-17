func superPow(a int, b []int) int {
	if len(b) == 1 {
		return helper(a, b[0])
	} else {
		return merge(superPow(helper(a, 10), b[0:len(b)-1]), helper(a, b[len(b)-1]))
	}
}

func merge(a, b int) int {
	return ((a % 1337) * (b % 1337)) % 1337
}

func helper(a, power int) int {
	if power == 0 {
		return 1
	}
	return merge(a%1337, helper(a, power-1))
}
