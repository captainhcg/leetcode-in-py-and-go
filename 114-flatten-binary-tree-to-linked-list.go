/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

var pre *TreeNode
func flatten(root *TreeNode) {
	pre = nil
	helper(root)
}

func helper(nd *TreeNode) {
	if nd == nil {
		return
	}
	fmt.Println(nd.Val)
	if pre == nil {
		pre = nd
	} else {
		pre.Right = nd
		pre = nd
	}
	left := nd.Left
	right := nd.Right
	nd.Left = nil
	nd.Right = nil
	helper(left)
	helper(right)
}
