func isPalindrome(x int) bool {
    if x < 0{
        return false
    }
    y := x
    rev := 0
    for ; y > 0; {
        a := y % 10
        rev = rev * 10 + a
        y = y / 10
    }
    return rev == x
}
