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
    p1 := l1
    p2 := l2
    for p1 != nil && p2 != nil {
        var small *ListNode
        if p1.Val < p2.Val{
            small = p1
            p1 = p1.Next
        } else {
            small = p2
            p2 = p2.Next
        }
        pre.Next = small
        pre = small
    }
    if p2 == nil {
        pre.Next = p1
    } else {
        pre.Next = p2
    }
    return head.Next
}
