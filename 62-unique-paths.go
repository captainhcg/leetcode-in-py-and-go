func uniquePaths(m int, n int) int {
    if m == 1 || n == 1 {
        return 1
    }
    if m > n {
        return c(m+n-2, n-1)
    }
    return c(m+n-2, m-1)
}

func c(m, n int) int {
    divident := 1
    for i := m; i > m - n; i-- {
        divident *= i
    }
    for i := n; i > 0; i-- {
        divident /= i
    }
    return divident
}
