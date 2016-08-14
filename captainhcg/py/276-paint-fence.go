func numWays(n int, k int) int {
    arr := []int{0, k, k*k}
    if n <= 2{
        return arr[n]
    }
    for idx := 3; idx <=n; idx+=1{
        arr = append(arr, (k-1) * (arr[idx-2] + arr[idx-1]))
    }
    return arr[n]
}
