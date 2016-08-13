/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sortedArrayToBST(nums []int) *TreeNode {
    if len(nums) == 0{
        return nil
    }
    return makeNode(nums, 0, len(nums)-1)
}

func makeNode(nums[] int, left, right int) *TreeNode{
    if right < left{
        return nil
    }
    mid := (left + right) / 2
    nd := &TreeNode{nums[mid], nil, nil}
    nd.Left = makeNode(nums, left, mid-1)
    nd.Right = makeNode(nums, mid+1, right)
    return nd
}
