func check(grid [][]int, y int, x int) bool{
    if y < 0 || x < 0 || y >= len(grid) || x >= len(grid[0]){
        return true
    }
    return grid[y][x] == 0
}

func islandPerimeter(grid [][]int) int {
    if len(grid) == 0 {
        return 0
    }
    cnt := 0
    for i:=0; i<len(grid); i+=1{
        for j:=0; j < len(grid[0]); j+=1{
            if grid[i][j] == 0{
                continue
            }
            if check(grid, i+1, j){
                cnt += 1
            }
            if check(grid, i, j+1){
                cnt += 1
            }
            if check(grid, i-1, j){
                cnt += 1
            }
            if check(grid, i, j-1){
                cnt += 1
            }
        }
    }
    return cnt
}
