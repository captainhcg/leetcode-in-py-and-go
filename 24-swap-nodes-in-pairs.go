/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func swapPairs(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head
    }
    first := head
    second := first.Next
    third := second.Next
    first.Next = swapPairs(third)
    second.Next = first
    return second
}
