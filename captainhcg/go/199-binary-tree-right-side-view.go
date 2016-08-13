/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
var ret []int
func rightSideView(root *TreeNode) []int {
    ret = make([]int, 0)
    if root == nil{
        return ret
    }
    helper(root, 0)
    return ret
}

func helper(nd *TreeNode, level int){
    if nd == nil{
        return
    }
    if len(ret) <= level{
        ret = append(ret, 0)
    }
    ret[level] = nd.Val
    helper(nd.Left, level+1)
    helper(nd.Right, level+1)
}
