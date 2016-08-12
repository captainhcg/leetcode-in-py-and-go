/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reorderList(head *ListNode)  {
    if head == nil || head.Next == nil{
        return
    }
    // 1->2->3->4->5
    lead := &ListNode{-1, head}
    // -1->1->2->3->4->5
    slow, fast, newFast := lead, lead, getTail(lead)
    for fast != nil && fast.Next != nil{
        slow = slow.Next
        fast = fast.Next
        fast = fast.Next
    }
    // slow: 3/ fast: nil/ newFast: 5
    
    new_tail := reverseNode(slow.Next)
    new_tail.Next, slow.Next = nil, nil
    // new_tail: 4/ 4.Next = nil/ 3.Next = nil
    
    combine(lead.Next, newFast)
}

func combine(left *ListNode, right *ListNode) *ListNode{
    // 1->2->3 & 5->4 => 1->5->2->4->3
    var rNext *ListNode
    if left.Next != nil{
        rNext = combine(left.Next, right.Next)
    }
    left.Next = right
    if right != nil{
        right.Next = rNext
    }
    return left
}

func getTail(nd *ListNode) *ListNode{
    for nd.Next != nil {
        nd = nd.Next
    }
    return nd
}

func reverseNode(nd *ListNode) *ListNode{
    if nd != nil{
        next := reverseNode(nd.Next)
        if next != nil{
            next.Next = nd
        }
    }
    return nd
}
