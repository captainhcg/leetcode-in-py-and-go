func reverse(pre *ListNode, k int) *ListNode {
    checkNode := pre.Next
    for idx := 0; idx < k; idx += 1 {
        if checkNode == nil{
            return nil
        }
        checkNode=checkNode.Next
    }
    
    start, end := pre.Next, pre.Next
    for idx := 0; idx < k - 1; idx += 1{
        oldStart := start
        start, end.Next = end.Next, end.Next.Next
        pre.Next, start.Next = start, oldStart
    }
    return end
} 

func reverseKGroup(head *ListNode, k int) *ListNode {
    if k <= 1{
        return head
    }
    dummy := &ListNode{-1, head}
    for nextPre := dummy; nextPre != nil; {
        nextPre = reverse(nextPre, k)
    }
    return dummy.Next
}
