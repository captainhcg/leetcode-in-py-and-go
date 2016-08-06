/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
var res []int

func inorderTraversal(root *TreeNode) []int {
    res = make([]int, 0)
    tra(root)
    return res  
}

func tra(node *TreeNode){
    if node == nil{
        return
    }
    tra(node.Left)
    res = append(res, node.Val)
    tra(node.Right)
}
