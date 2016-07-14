/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
    if l1 == nil{
        return l2
    } else if l2 == nil{
        return l1
    }
    head := &ListNode{}
    pre := head
    for l1 != nil && l2 != nil {
        var small *ListNode
        if l1.Val < l2.Val{
            small = l1
            l1 = l1.Next
        } else {
            small = l2
            l2 = l2.Next
        }
        pre.Next = small
        pre = small
    }
    if l2 == nil {
        pre.Next = l1
    } else {
        pre.Next = l2
    }
    return head.Next
}
