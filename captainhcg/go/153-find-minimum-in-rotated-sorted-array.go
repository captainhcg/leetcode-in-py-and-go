func findMin(nums []int) int {
    return helper(nums, 0, len(nums)-1)
}

func helper(nums []int, st, ed int) int {
    if (st == ed) {
        return nums[st]
    }
    mid := (st + ed) / 2
    if nums[mid] > nums[ed]{
        return helper(nums, mid+1, ed)
    }
    return helper(nums, st, mid)
}
