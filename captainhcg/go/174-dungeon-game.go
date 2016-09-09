func min(a, b int) int{
    if a < b{
        return a
    }
    return b
}

func max(a, b int) int{
    if a > b{
        return a
    }
    return b
}

func calculateMinimumHP(dungeon [][]int) int {
	mat := make([][]int, len(dungeon))
	for idx := range dungeon {
		mat[idx] = make([]int, len(dungeon[0]))
	}
	for row := len(dungeon) - 1; row >= 0; row -= 1 {
		for col := len(dungeon[0]) - 1; col >= 0; col -= 1 {
			var minhp int
			if row == len(dungeon)-1 && col == len(dungeon[0])-1 {
				minhp = -dungeon[row][col]
			} else if row == len(dungeon)-1 {
				minhp = -dungeon[row][col] + mat[row][col+1]
			} else if col == len(dungeon[0])-1 {
				minhp = -dungeon[row][col] + mat[row+1][col]
			} else {
				minhp = -dungeon[row][col] + min(mat[row+1][col], mat[row][col+1])
			}
			mat[row][col] = max(minhp, 0)
		}
	}
	return mat[0][0] + 1
}
