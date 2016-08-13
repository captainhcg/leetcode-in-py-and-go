func isPerfectSquare(num int) bool {
    st := 1
    sum := st
    for sum <= num{
        if sum == num{
            return true
        }
        st += 2
        sum += st
    }
    return false
}
