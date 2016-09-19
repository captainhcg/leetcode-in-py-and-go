type MyPoint struct {
	X int
	Y int
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

var cntMap map[MyPoint]int

func addPoint(x, y int) {
	p := MyPoint{x, y}
	_, valid := cntMap[p]
	if valid {
		cntMap[p] += 1
	} else {
		cntMap[p] = 1
	}
}

func isRectangleCover(rectangles [][]int) bool {
	cntMap = make(map[MyPoint]int)
	minX, minY, maxX, maxY := 1<<30, 1<<30, -1<<30, -1<<30
	area := 0
	for _, point := range rectangles {
		x1, x2, y1, y2 := point[0], point[2], point[1], point[3]
		minX = min(x1, minX)
		maxX = max(x2, maxX)
		minY = min(y1, minY)
		maxY = max(y2, maxY)
		addPoint(x1, y1)
		addPoint(x2, y1)
		addPoint(x1, y2)
		addPoint(x2, y2)
		area += (x2 - x1) * (y2 - y1)
	}
	if area != (maxX-minX)*(maxY-minY) {
		return false
	}
	for _, point := range [][]int{{minX, minY}, {minX, maxY}, {maxX, minY}, {maxX, maxY}} {
		pt := MyPoint{point[0], point[1]}
		cnt, _ := cntMap[pt]
		if cnt != 1 {
			return false
		}
		delete(cntMap, pt)
	}
	for _, v := range cntMap {
		if v != 2 && v != 4 {
			return false
		}
	}
	return true
}
