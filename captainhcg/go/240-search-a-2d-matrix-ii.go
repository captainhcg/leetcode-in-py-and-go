func searchMatrix(matrix [][]int, target int) bool {
    if len(matrix) == 0 || len(matrix[0]) == 0{
        return false
    }
    row := 0
    col := len(matrix[0]) - 1
    for col >= 0 && row < len(matrix){
        v := matrix[row][col]
        if v == target{
            return true
        } else if v > target {
            col -= 1
        } else {
            row += 1
        }
        
    }
    return false
}
