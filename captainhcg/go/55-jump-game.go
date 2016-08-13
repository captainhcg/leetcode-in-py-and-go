func canJump(nums []int) bool {
    furthest := 0
    for idx, n := range(nums){
        if furthest < idx{
            break
        }
        furthest = max(n+idx, furthest)
    }
    return furthest >= len(nums) - 1
}

func max(a, b int) int{
    if a > b{
        return a
    }
    return b
}
