func numDistinct(s string, t string) int {
    dp := make([][]int, len(t) + 1)
    for idx := 0; idx < len(dp); idx += 1{
        dp[idx] = make([]int, len(s) + 1)
    }
    for idx := range dp[0]{
        dp[0][idx] = 1
    }
    for y := 1; y <= len(t); y += 1{
        for x := 1; x <= len(s); x += 1{
            if t[y-1] == s[x-1]{
                dp[y][x] = dp[y][x-1] + dp[y-1][x-1]
            } else {
                dp[y][x] = dp[y][x-1]
            }
        }
    }
    return dp[len(t)][len(s)]
}
