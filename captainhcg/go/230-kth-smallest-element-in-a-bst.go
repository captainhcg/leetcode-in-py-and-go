/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
var cnt int
var nd *TreeNode

func kthSmallest(root *TreeNode, k int) int {
    cnt = 0
    nd = nil
    tra(root, k)
    return nd.Val
}

func tra(node *TreeNode, k int){
    if node == nil || nd != nil{
        return
    }
    tra(node.Left, k)
    cnt += 1
    if cnt == k{
        nd = node
    }
    tra(node.Right, k)
}
