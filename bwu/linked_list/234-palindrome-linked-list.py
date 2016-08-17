# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
            
        end1, head2 = self.findMid(head)
        new_head = head2
        
        if end1 == head2:
            new_head = ListNode(end1.val)
            new_head.next = head2.next
            head2 = new_head
            
        end1.next = None
        
        head = self.reverse(head)
        p, q = head, new_head
        while p and q:
            if p.val != q.val:
                return False
            else:
                p = p.next
                q = q.next
                
        if p or q:
            return False
        return True
        
    def findMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            return slow, slow.next
        else:
            return slow, slow
            
    def reverse(self, head):
        tail = None
        p = head
        while p:
            tmp = p.next
            p.next = tail
            tail = p
            p = tmp
        return tail
