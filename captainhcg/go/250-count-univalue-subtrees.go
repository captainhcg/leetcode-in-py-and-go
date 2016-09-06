var cnt int

func helper(node, parent *TreeNode) bool {
	if node == nil {
		return true
	}
	left_result, right_result := helper(node.Left, node), helper(node.Right, node)
	if left_result && right_result {
		cnt += 1
		if parent != nil && node.Val == parent.Val {
			return true
		}
	}
	return false
}

func countUnivalSubtrees(root *TreeNode) int {
	cnt = 0
	helper(root, nil)
	return cnt
}
