# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        curr = dummy
        curr.next = head
        
        while curr.next and curr.next.next:
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = curr.next.next
            curr.next.next = tmp
            curr = tmp
        return dummy.next
