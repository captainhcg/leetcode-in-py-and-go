/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func rotateRight(head *ListNode, k int) *ListNode {
    if head == nil || head.Next == nil{
        return head
    }
    tail := head
    length := 1
    for tail.Next != nil{
        tail = tail.Next
        length += 1
    }
    tail.Next = head
    k = k % length
    if k > 0{
        cnt := length - k
        for cnt > 0{
            tail = head
            head = head.Next
            cnt -= 1
        }
    }
    tail.Next = nil
    return head
}
