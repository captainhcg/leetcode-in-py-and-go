/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
var res []int

func preorderTraversal(root *TreeNode) []int {
    res = make([]int, 0)
    tra(root)
    return res
}

func tra(node *TreeNode){
    if node == nil{
        return
    }
    res = append(res, node.Val)
    tra(node.Left)
    tra(node.Right)
}
