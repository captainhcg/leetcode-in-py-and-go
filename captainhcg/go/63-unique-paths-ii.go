func uniquePathsWithObstacles(obstacleGrid [][]int) int {
    h := len(obstacleGrid)
    if h == 0 {
        return 0
    }
    w := len(obstacleGrid[0])
    if w == 0 {
        return 0
    }
    for y := 0; y < h; y += 1{
        for x := 0; x < w; x += 1{
            if x == 0 && y == 0 {
                if obstacleGrid[y][x] == 1{
                    obstacleGrid[y][x] = 0
                } else {
                    obstacleGrid[y][x] = 1
                }
                continue
            }
            if obstacleGrid[y][x] == 1 {
                obstacleGrid[y][x] = 0
            } else {
                if y > 0 {
                    obstacleGrid[y][x] += obstacleGrid[y-1][x]
                }
                if x > 0 {
                    obstacleGrid[y][x] += obstacleGrid[y][x-1]
                }
            }
        }
    }
    return obstacleGrid[h-1][w-1]
}
