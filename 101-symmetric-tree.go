/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSymmetric(root *TreeNode) bool {
    if root == nil{
        return true
    }
    return symHelper(root.Left, root.Right)
}

func symHelper(left *TreeNode, right *TreeNode) bool {
    if left == nil && right == nil {
        return true
    }
    if left == nil || right == nil {
        return false
    }
    if left.Val != right.Val {
        return false
    }
    return symHelper(left.Left, right.Right) && symHelper(left.Right, right.Left)
}
