func deleteDuplicates(head *ListNode) *ListNode {
    var pre, ret, tail *ListNode
    for head != nil{
        if (pre == nil || pre.Val != head.Val) && (head.Next == nil || head.Next.Val != head.Val ){
            if ret == nil{
                ret = head
                tail = head
            } else {
                tail.Next = head
                tail = head
            }
        }
        pre = head
        head = head.Next
    }
    if ret == nil{
        return nil
    } else {
        tail.Next = nil
        return ret
    }
}
