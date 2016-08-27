# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return head
            
        dummy = ListNode(0)
        dummy.next = head
        dummy2 = ListNode(0)
        lp = dummy2
        prev, curr = dummy, head
        
        while curr:
            if curr.val < x:
                lp.next = curr
                lp = lp.next
                prev.next = curr.next
                curr = prev.next
            else:
                prev = curr
                curr = curr.next
                
        lp.next = dummy.next
        return dummy2.next
