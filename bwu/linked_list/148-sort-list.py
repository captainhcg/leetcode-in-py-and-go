# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
           
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre = slow
            fast = fast.next.next
            slow = slow.next
            
        pre.next = None
        
        left = self.sortList(head)
        right = self.sortList(slow)
        return self.merge(left, right)

    def merge(self, p, q):
        dummy = ListNode(0)
        curr = dummy
        while p and q:
            if p.val < q.val:
                curr.next = p
                p = p.next
            else:
                curr.next = q
                q = q.next
            curr = curr.next
                
        if p:
            curr.next = p
        if q:
            curr.next = q
            
        return dummy.next
            
