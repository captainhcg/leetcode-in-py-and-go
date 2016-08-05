func removeElements(head *ListNode, val int) *ListNode {
    header := &ListNode{0, head}
    pre := header
    cur := head
    for cur != nil{
        if cur.Val != val{
            pre = cur
        } else {
            pre.Next = cur.Next
        }
        cur = cur.Next
    }
    return header.Next
}
