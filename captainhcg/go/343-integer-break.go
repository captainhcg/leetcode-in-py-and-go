func integerBreak(n int) int {
    if n == 2{
        return 1
    }
    if n == 3{
        return 2
    }
    if n == 4{
        return 4
    }
    base := 1
    for n > 4 {
        base = base * 3
        n -= 3
    }
    base *= n
    return base
}
