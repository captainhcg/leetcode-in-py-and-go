func verifyPreorder(preorder []int) bool {
	if len(preorder) < 2 {
		return true
	}
	pivot := preorder[0]
	small_idx := 0
	for _, n := range preorder[1:] {
		if n < pivot {
			small_idx += 1
		} else {
			break
		}
	}
	for _, n := range preorder[1+small_idx:] {
		if n < pivot {
			return false
		}
	}
	return verifyPreorder(preorder[1:1+small_idx]) && verifyPreorder(preorder[1+small_idx:])
}
