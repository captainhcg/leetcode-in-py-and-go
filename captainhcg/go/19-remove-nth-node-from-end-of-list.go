/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    pre := &ListNode{}
    pre.Next = head
    header := pre
    fast := head
    for n > 1 {
        fast = fast.Next
        n -= 1
    }
    for fast.Next != nil {
        fast = fast.Next
        pre = pre.Next
    }
    pre.Next = pre.Next.Next
    return header.Next
}
