func numTrees(n int) int {
    if n == 0{
        return 0
    }
    if n == 1{
        return 1
    }
    if n == 2{
        return 2
    }
    arr := make([]int, n+1)
    arr[0] = 1
    arr[1] = 1
    arr[2] = 2
    for idx := 3; idx <= n; idx += 1{
        for jdx := 1; jdx <= idx; jdx += 1 {
            arr[idx] += arr[jdx-1] * arr[idx-jdx]
        }
    }
    return arr[n]
}
