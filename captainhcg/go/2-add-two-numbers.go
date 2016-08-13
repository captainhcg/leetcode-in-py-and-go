/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    carry := false
    header := &ListNode{}
    last := header
    for l1 != nil || l2 != nil || carry {
        cur := 0;
        if carry {
            cur += 1 
        }
        if l1 != nil {
            cur += l1.Val
            l1 = l1.Next
        }
        if l2 != nil {
            cur += l2.Val
            l2 = l2.Next
        }
        if cur >= 10 {
            carry = true
            cur -= 10
        } else {
            carry = false
        }
        last.Next = &ListNode{cur, nil}
        last = last.Next
    }
    return header.Next
}
