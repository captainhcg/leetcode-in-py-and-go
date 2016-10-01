# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not k or not head:
            return head
            
        dummy = ListNode(0)
        dummy.next = head
        tail = dummy
        length = 0
        while tail.next:
            tail = tail.next
            length += 1
            
        if k % length == 0:
            return head
            
        slow, fast = dummy, dummy
        for i in xrange(k % length):
            fast = fast.next
            
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        dummy.next = slow.next
        slow.next = None
        fast.next = head
        return dummy.next
