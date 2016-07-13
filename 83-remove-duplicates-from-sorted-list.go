/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	pre := head
	cur := head.Next
	for cur != nil {
		if cur.Val != pre.Val {
			pre = cur
		} else {
			pre.Next = cur.Next
		}
		cur = cur.Next
	}
	return head
}
