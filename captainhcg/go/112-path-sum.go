/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func hasPathSum(root *TreeNode, sum int) bool {
    return hasPathSumHelper(root, 0, sum)
}
func hasPathSumHelper(node *TreeNode, sum, target int) bool{
    if node == nil{
        return false
    }
    if node.Val + sum == target && isLeaf(node){
        return true
    }
    return hasPathSumHelper(node.Left, node.Val + sum, target) || hasPathSumHelper(node.Right, node.Val + sum, target)
}
func isLeaf(node *TreeNode) bool{
    return node.Left == nil && node.Right == nil
}
