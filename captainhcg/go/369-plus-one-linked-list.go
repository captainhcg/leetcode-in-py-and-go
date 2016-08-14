func plusOne(head *ListNode) *ListNode {
    dummy := &ListNode{0, head}
    process(dummy)
    if dummy.Val == 1{
        return dummy
    } else {
        return dummy.Next
    }
}

func process(nd *ListNode) int {
    var carry, val int
    if nd.Next == nil{
        carry, val = 0, nd.Val + 1
    } else {
        carry, val = process(nd.Next), nd.Val
    }
    if carry + val >= 10{
        val = carry + val - 10
        carry = 1
    } else {
        val = carry + val
        carry = 0
    }
    nd.Val = val
    return carry
}
