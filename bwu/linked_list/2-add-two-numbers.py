# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
            
        dummy = ListNode(0)
        res = dummy
        p1, p2 = l1, l2
        carrier = 0
        
        while p1 and p2:
            tmp = p1.val + p2.val + carrier
            carrier = tmp / 10
            node = ListNode(tmp % 10)
            p1 = p1.next
            p2 = p2.next
            res.next = node
            res = res.next
            
        while p1:
            tmp = p1.val + carrier
            carrier = tmp / 10
            node = ListNode(tmp % 10)
            res.next = node
            res = res.next
            p1 = p1.next
            
        while p2:
            tmp = p2.val + carrier
            node = ListNode(tmp % 10)
            res.next = node
            res = res.next
            carrier = tmp / 10
            p2 = p2.next
            
        if carrier:
            node = ListNode(1)
            res.next = node
            
        return dummy.next
