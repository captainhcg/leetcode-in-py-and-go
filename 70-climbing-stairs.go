func climbStairs(n int) int {
    if n == 1{
        return 1
    } else if n == 2{
        return 2
    }
    steps := make([]int, n)
    steps[0], steps[1] = 1, 2 
    for idx := 2; idx < n; idx++ {
        steps[idx] = steps[idx-1] + steps[idx-2]
    }
    return steps[n-1]
}
