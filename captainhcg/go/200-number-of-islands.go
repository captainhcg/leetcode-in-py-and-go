func numIslands(grid [][]byte) int {
    cnt := 0
    for x:= 0; x<len(grid); x+= 1{
        for y:=0; y < len(grid[0]); y+=1 {
            if grid[x][y] == '1'{
                cnt += 1
                flip(x, y, grid)
            }
        }
    }
    return cnt
}

func flip(x, y int, grid [][]byte){
    if x < 0 || x >= len(grid) || y < 0 || y >= len(grid[0]){
        return
    }
    if grid[x][y] == '0'{
        return
    }
    grid[x][y] = '0'
    flip(x+1, y, grid)
    flip(x-1, y, grid)
    flip(x, y-1, grid)
    flip(x, y+1, grid)
}
