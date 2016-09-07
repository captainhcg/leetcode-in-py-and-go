func reverseBetween(head *ListNode, m int, n int) *ListNode {
	dummy := &ListNode{0, head}
	pre := dummy
	for i := 1; i < m; i += 1 {
		pre = pre.Next
	}
	start, end := pre.Next, pre.Next
	for i := 0; i < n-m; i += 1 {
		oldStart := start
		start, end.Next = end.Next, end.Next.Next
		start.Next, pre.Next = oldStart, start
	}
	return dummy.Next
}
