/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func minDepthHelper(small, large int) int {
    // small and large cannot both be 0
    if small == 0 {
        return large + 1
    }
    return small + 1
}

func minDepth(root *TreeNode) int {
    if root == nil {
        return 0
    }
    left, right := minDepth(root.Right), minDepth(root.Left)
    if left > right {
        return minDepthHelper(right, left)
    } else {
        return minDepthHelper(left, right)
    }
}
