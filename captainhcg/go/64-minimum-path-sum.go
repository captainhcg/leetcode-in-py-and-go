func minPathSum(grid [][]int) int {
    matrix := make([][]int, len(grid))
    for idx := 0; idx < len(grid); idx += 1{
        matrix[idx] = make([]int, len(grid[0]))
    }
    matrix[0][0] = grid[0][0]
    for idx := 1; idx < len(grid); idx += 1{
        matrix[idx][0] = grid[idx][0] + matrix[idx-1][0]
    }
    for jdx := 1; jdx < len(grid[0]); jdx += 1{
        matrix[0][jdx] = grid[0][jdx] + matrix[0][jdx-1]
    }
    
    for idx := 1; idx < len(grid); idx += 1{
        for jdx := 1; jdx < len(grid[0]); jdx += 1{
            matrix[idx][jdx] = grid[idx][jdx] + min(matrix[idx-1][jdx], matrix[idx][jdx-1])
        }
    }
    return matrix[len(grid)-1][len(grid[0])-1]
}

func min(a, b int) int{
    if a < b {
        return a
    }
    return b
}
