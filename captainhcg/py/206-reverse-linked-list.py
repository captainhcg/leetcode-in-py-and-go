# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # return self.reverse_helper_recur(None, head)
        return self.reverse_helper_iter(head)
    
    def reverse_helper_iter(self, head):
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
    
    def reverse_helper_recur(self, pre, cur):
        if not cur:
            return pre
        next = cur.next
        cur.next = pre
        return self.reverse_helper_iter(cur, next)
