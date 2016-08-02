func minDistance(word1 string, word2 string) int {
    if len(word1) == 0{
        return len(word2)
    }
    if len(word2) == 0{
        return len(word1)
    }
    N, M := len(word1) + 1, len(word2) + 1
    mat := make([][]int, N)
    for i := 0; i < N; i++{
        mat[i] = make([]int, M)
    }
    for i := 0; i < N; i++{
        mat[i][0] = i
    }
    for i := 0; i < M; i++{
        mat[0][i] = i
    }
    for i := 1; i < N; i++{
        for j := 1; j < M; j++ {
            if word1[i-1] == word2[j-1]{
                mat[i][j] = mat[i-1][j-1]
            } else {
                mat[i][j] = getMin(mat[i-1][j-1] + 1, mat[i-1][j] + 1, mat[i][j-1] + 1)
            }
        }
    }
    return mat[N-1][M-1]
}

func getMin(n1, n2, n3 int) int{
    min := n1
    if n2 < min{
        min = n2
    }
    if n3 < min {
        min = n3
    }
    return min
}
