func nextPermutation(nums []int) {
	if len(nums) == 1 {
		return
	}
	swap_big := len(nums) - 1
	for swap_big > 0 {
		swap_small := swap_big - 1
		if nums[swap_small] < nums[swap_big] {
			for to_swap := len(nums) - 1; to_swap > swap_small; to_swap -= 1 {
				if nums[to_swap] > nums[swap_small] {
					nums[to_swap], nums[swap_small] = nums[swap_small], nums[to_swap]
					sort.Ints(nums[swap_small+1 : len(nums)])
					return
				}
			}
		}
		swap_big -= 1
	}
	sort.Ints(nums)
	return
}
