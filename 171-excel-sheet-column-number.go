func titleToNumber(s string) int {
    // If there is easy(builtin) way to reverse string in go then the code can be much cleaner
    ret := 0
    chars := []byte(s)
    length := len(chars)
    for i := 0; i < length; i += 1{
        char := chars[i]
        ret += int(char - 'A' + 1) * int(math.Pow(26, float64(length - i - 1)))
    }
    return ret
}
