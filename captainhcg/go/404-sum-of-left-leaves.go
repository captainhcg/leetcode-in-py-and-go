var ret int
func sumOfLeftLeaves(root *TreeNode) int {
    ret = 0
    var helper func(node *TreeNode, isLeft bool)
    helper = func(node *TreeNode, isLeft bool) {
        if node.Left == nil && node.Right == nil{
            if isLeft{
                ret += node.Val
            }
            return
        }
        if node.Left != nil{
            helper(node.Left, true)
        }
        if node.Right != nil{
            helper(node.Right, false)
        }
    }
    if root != nil {
        helper(root, false)
    }
    return ret
}
