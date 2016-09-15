var mat[][] int
func getMoneyAmount(n int) int {
    mat = make([][]int, n+1)
    for idx := 0; idx <= n; idx += 1{
        mat[idx] = make([]int, n+1)
    }
    dfs(1, n)
    return mat[1][n]
}

func min(a, b int) int {
    if a < b{
        return a
    }
    return b
}

func max(a, b int) int {
    if a > b{
        return a
    }
    return b
}

func dfs(st, ed int) int{
    if st >= ed{
        return 0
    } else if(mat[st][ed] != 0){
        return mat[st][ed]
    }
    minP := (1 << 30)
    for mid := st; mid <= ed; mid += 1{
        left := dfs(st, mid-1)
        right := dfs(mid+1, ed)
        minP = min(max(left, right) + mid, minP)
    }
    mat[st][ed] = minP
    return minP
}
