/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func isPalindrome(head *ListNode) bool {
    if(head == nil){
        return true
    }
    arr := make([]int, 0)
    for head != nil{
        arr = append(arr, head.Val)
        head = head.Next
    }
    start, end := 0, len(arr)-1
    for start < end{
        if arr[start] != arr[end]{
            return false
        }
        start += 1
        end -= 1
    }
    return true
}
