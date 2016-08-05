func trailingZeroes(n int) int {
    base := 5
    sum := 0
    for n >= base {
        sum += n / base
        base *= 5
    } 
    return sum
}
