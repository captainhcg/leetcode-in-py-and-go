func singleNumber(nums []int) []int {
    res := 0
    for _, n := range nums{
        res ^= n
    }
    bit := res & (-res)
    n1, n2 := 0, 0
    for _, n := range nums{
        if bit & n == 0{
            n1 ^= n 
        } else {
            n2 ^= n
        }
    }
    return []int{n1, n2}
}
