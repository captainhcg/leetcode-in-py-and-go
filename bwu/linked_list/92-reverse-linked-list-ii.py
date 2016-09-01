# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        curr = dummy.next
        
        while curr and m > 1:
            curr = curr.next
            start = start.next
            m -= 1
            n -= 1
            
        while curr.next and n > 1:
            tmp = start.next
            new_next  = curr.next
            start.next = new_next
            curr.next = new_next.next
            new_next.next = tmp
            n -= 1
            
        return dummy.next
