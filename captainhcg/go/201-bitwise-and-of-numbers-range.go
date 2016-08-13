func rangeBitwiseAnd(m int, n int) int {
    for n > m{
        n = n & (n-1)
    }
    return n
}
