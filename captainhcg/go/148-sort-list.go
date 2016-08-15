func sortList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	dummy, middle := &ListNode{}, findMiddle(head)
	pre := dummy
	n1, n2 := sortList(head), sortList(middle)
	for n1 != nil && n2 != nil {
		if n1.Val <= n2.Val {
			pre.Next, pre, n1 = n1, n1, n1.Next
		} else {
			pre.Next, pre, n2 = n2, n2, n2.Next
		}
	}
	for n1 != nil {
		pre.Next, pre, n1 = n1, n1, n1.Next
	}
	pre.Next = n2
	return dummy.Next
}

func findMiddle(node *ListNode) *ListNode {
	if node.Next == nil {
		return node
	}
	slow, fast := node, node
	for fast.Next != nil && fast.Next.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	ret := slow.Next
	slow.Next = nil
	return ret
}
