# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
            
        odd, even = head, head.next
        dummy1, dummy2 = ListNode(0), ListNode(0)
        dummy1.next = odd
        dummy2.next = even
        
        while odd.next and even.next:
            if odd.next == even:
                odd.next = even.next
                odd = odd.next
            else:
                even.next = odd.next
                even = even.next
        
        if even.next == odd:
            even.next = odd.next
            
        odd.next = dummy2.next
        return dummy1.next
