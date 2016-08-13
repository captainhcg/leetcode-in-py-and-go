func addDigits(num int) int {
    if num == 0 {
        return 0
    }
    if rd := num % 9; rd == 0{
        return 9
    } else {
        return rd
    }
}
