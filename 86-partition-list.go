/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func partition(head *ListNode, x int) *ListNode {
    if head == nil{
        return head
    }
    var bh, bc, sh, sc *ListNode
    nd := head
    for nd != nil{
        if nd.Val < x{
            if sh == nil{
                sh = nd
                sc = nd
            } else {
                sc.Next = nd
                sc = nd
            }
        } else {
            if bh == nil{
                bh = nd
                bc = nd
            } else {
                bc.Next = nd
                bc = nd
            }
        }
        nd = nd.Next
    }
    if sc != nil {
        sc.Next = bh
    }
    if bc != nil {
        bc.Next = nil
    }
    if sh != nil{
        return sh
    }
    return bh
}
