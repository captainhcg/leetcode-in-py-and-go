var cache []int

func combinationSum4(nums []int, target int) int {
    cache = make([]int, target + 1)
    cache[0] = 1
    for idx := 1; idx <= target; idx += 1{
        cache[idx] = -1
    }
    return helper(nums, target)
}

func helper(nums []int, target int) int {
    if cache[target] != -1{
        return cache[target]
    }
    ret := 0
    for _, n := range nums{
        if target >= n{
            ret += helper(nums, target-n)
        }
    }
    cache[target] = ret
    return ret
}
