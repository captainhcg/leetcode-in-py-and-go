type Direction struct {
	x int
	y int
}

func spiralOrder(matrix [][]int) []int {
	result := make([]int, 0)
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return result
	}
	directions := []Direction{
		Direction{1, 0},
		Direction{0, 1},
		Direction{-1, 0},
		Direction{0, -1},
	}
	curX, curY, direction := 0, 0, 0
	rows, cols := len(matrix), len(matrix[0])
	top, bottom, left, right := 0, rows-1, 0, cols-1
	for true {
		result = append(result, matrix[curY][curX])
		if len(result) == rows*cols {
			break
		}
		getNext := false
		for getNext == false {
			dir := directions[direction]
			newX, newY := curX+dir.x, curY+dir.y
			if newX <= right && newX >= left && newY <= bottom && newY >= top {
				curX, curY = newX, newY
				getNext = true
			} else {
				if newX > right {
					top += 1
				} else if newX < left {
					bottom -= 1
				} else if newY > bottom {
					right -= 1
				} else {
					left += 1
				}
				direction = (direction + 1) % 4
			}
		}
	}
	return result
}
