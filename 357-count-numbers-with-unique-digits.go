var m = make(map[int]int)
func F(n int) int {
    res, ok := m[n]
    if ok{
        return res
    }
    if n == 1{
        res = 10
    } else if n <= 10 {
        res = 9
        for cnt := n - 1; cnt >= 1; cnt -= 1{
            res *= (10 - cnt)
        } 
        
    } else {
        res = 0
    }
    m[n] = res
    return res
}

func countNumbersWithUniqueDigits(n int) int {
    if n == 0 {
        return 1
    }
    res := 0
    for ; n > 0; n -= 1{
        res += F(n)
    }
    return res 
}
