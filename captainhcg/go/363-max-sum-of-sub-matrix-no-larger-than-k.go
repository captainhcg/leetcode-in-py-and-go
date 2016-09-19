func max(n1, n2 int) int {
	if n2 > n1 {
		return n2
	}
	return n1
}

func min(n1, n2 int) int {
	if n2 < n1 {
		return n2
	}
	return n1
}

type Node struct {
	Val   int
	Left  *Node
	Right *Node
}

type Value struct {
	Val int
}

func findMinBigger(node *Node, val int) *Value {
	if node.Val == val {
		return &Value{node.Val}
	}
	var other *Value
	if node.Val > val && node.Left != nil {
		other = findMinBigger(node.Left, val)
	} else if node.Val < val && node.Right != nil {
		other = findMinBigger(node.Right, val)
	}
	if other != nil {
		if node.Val >= val {
			return &Value{min(node.Val, other.Val)}
		} else {
			return other
		}
	} else {
		if node.Val >= val {
			return &Value{node.Val}
		} else {
			return nil
		}
	}
}

func insert(node *Node, val int) {
	if node.Val == val {
		return
	} else if node.Val > val {
		if node.Left != nil {
			insert(node.Left, val)
		} else {
			node.Left = &Node{val, nil, nil}
		}
	} else {
		if node.Right != nil {
			insert(node.Right, val)
		} else {
			node.Right = &Node{val, nil, nil}
		}
	}
}

func getCloset(sum []int, k int) int {
	closest := 0 - (1 << 30)
	root := &Node{0, nil, nil}
	for _, v := range sum {
		lookFor := v - k
		value := findMinBigger(root, lookFor)
		var t int
		if value != nil {
			t = value.Val
		} else {
			t = 0
		}
		if v-t <= k {
			closest = max(closest, v-t)
		}
		insert(root, v)
	}
	return closest
}

func maxSumSubmatrix(matrix [][]int, k int) int {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return 0
	}
	fmt.Println(len(matrix))
	fmt.Println(len(matrix[0]))
	closest := 0 - (1 << 30)
	for colStart := 0; colStart < len(matrix[0]); colStart += 1 {
		tmpArr := make([]int, len(matrix))
		sumArr := make([]int, len(matrix))
		for col := colStart; col < len(matrix[0]); col += 1 {
			for row := 0; row < len(matrix); row += 1 {
				tmpArr[row] += matrix[row][col]
				sumArr[row] += matrix[row][col]
				if row == 0 {
					sumArr[row] = tmpArr[row]
				} else {
					sumArr[row] = tmpArr[row] + sumArr[row-1]
				}
			}
			tmpCloset := getCloset(sumArr, k)
			closest = max(closest, tmpCloset)
		}
	}
	return closest
}
