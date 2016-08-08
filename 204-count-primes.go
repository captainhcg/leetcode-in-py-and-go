func countPrimes(n int) int {
    arr := make([]int, n)
    count := 0
    for idx := 2; idx < n; idx += 1{
        if arr[idx] == 0{
            count += 1
            for jdx := 2; jdx * idx < n; jdx += 1{
                arr[jdx * idx] = 1
            }
        }
    }
    return count
}
