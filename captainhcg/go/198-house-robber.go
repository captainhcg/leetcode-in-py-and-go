func rob(nums []int) int {
    if len(nums) == 0{
        return 0
    }
    if len(nums) == 1{
        return nums[0]
    }
    max_v := make([]int, len(nums))
    for idx := 0; idx < len(nums); idx += 1{
        if idx == 0{
            max_v[idx] = nums[0]
        } else if idx == 1{
            max_v[idx] = max(nums[0], nums[1])
        } else {
            max_v[idx] = max(max_v[idx-1], max_v[idx-2] + nums[idx])
        }
    }
    return max(max_v[len(nums)-1], max_v[len(nums)-2])
}

func max(a, b int) int {
    if a > b{
        return a
    }
    return b
}
