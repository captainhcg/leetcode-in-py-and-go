func countBits(num int) []int {
    arr := make([]int, num+1)
    for idx := 0; idx <= num; idx += 1{
        arr[idx] = arr[idx >> 1] + idx & 1
    }
    return arr
}
