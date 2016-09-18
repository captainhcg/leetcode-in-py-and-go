func lastRemaining(n int) int {
    var helper func(num int, rev bool) int
    helper = func(num int, rev bool) int {
        if num == 1{
            return 1
        } else if rev == true {
            return helper(num >> 1, false) << 1 - 1 + (num & 1)
        } else {
            return helper(num >> 1, true) << 1
        }
        
    }
    return helper(n, false)
}
