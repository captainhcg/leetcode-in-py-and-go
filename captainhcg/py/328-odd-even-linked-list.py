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
        oddhead = None
        evenhead = None
        lastodd = None
        lasteven = None
        cnt = 1
        node = head
        while node:
            if cnt % 2 == 0:
                if cnt == 2:
                    evenhead = node
                    lasteven = node
                else:
                    lasteven.next = node
                    lasteven = node
            else:
                if cnt == 1 :
                    oddhead = node
                    lastodd = node
                else:
                    lastodd.next = node
                    lastodd = node
            node = node.next
            cnt += 1
        if lastodd:
            lastodd.next = None
        if lasteven:
            lasteven.next = None
        if lastodd and evenhead:
            lastodd.next = evenhead
        return oddhead
        
